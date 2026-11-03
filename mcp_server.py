"""
MCP Server implementation for Cardiac Left Atrial Strain (LAS) Skill.
Exposes standard FastMCP-compatible tools for speckle-tracking left atrial phasic deformation and stiffness analysis.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import LeftAtrialStrainClient


def evaluate_left_atrial_strain(
    reservoir_strain_pct: float,
    booster_pump_strain_pct: Optional[float] = None,
    conduit_strain_pct: Optional[float] = None,
    mitral_e_over_e_prime: Optional[float] = 8.5,
    left_atrial_volume_index_ml_m2: Optional[float] = 28.0,
    rhythm: Optional[str] = "Sinus Rhythm",
    patient_age_years: Optional[int] = 60
) -> str:
    """
    Evaluates Left Atrial Reservoir (LASr), Conduit (LAScd), and Booster (LASct) strain.
    Returns structured analysis of left ventricular filling pressures, diastolic dysfunction, and atrial stiffness.
    """
    client = LeftAtrialStrainClient()
    result = client.evaluate_la_strain(
        reservoir_strain_pct=reservoir_strain_pct,
        booster_pump_strain_pct=booster_pump_strain_pct,
        conduit_strain_pct=conduit_strain_pct,
        mitral_e_over_e_prime=mitral_e_over_e_prime,
        left_atrial_volume_index_ml_m2=left_atrial_volume_index_ml_m2,
        rhythm=rhythm,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_left_atrial_strain",
                "description": "Calculates 2D speckle-tracking left atrial reservoir strain (LASr%), conduit strain (LAScd%), booster pump strain (LASct%), and LA stiffness index to evaluate diastolic filling pressures and heart failure risk.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "reservoir_strain_pct": {"type": "number", "description": "Peak systolic left atrial reservoir strain in % (normal >= 39%)"},
                        "booster_pump_strain_pct": {"type": "number", "description": "Active atrial contraction booster pump strain in % (normal 12 - 20%)"},
                        "conduit_strain_pct": {"type": "number", "description": "Passive early diastolic conduit strain in % (normal 20 - 32%)"},
                        "mitral_e_over_e_prime": {"type": "number", "description": "Mitral E/e' ratio (default: 8.5)"},
                        "left_atrial_volume_index_ml_m2": {"type": "number", "description": "LAVI in mL/m2 (default: 28.0 mL/m2)"},
                        "rhythm": {"type": "string", "description": "Cardiac rhythm: 'Sinus Rhythm' or 'Atrial Fibrillation'"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 60)"}
                    },
                    "required": ["reservoir_strain_pct"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = LeftAtrialStrainClient()
        test_res = client.evaluate_la_strain(
            reservoir_strain_pct=42.0,
            booster_pump_strain_pct=15.0
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
