"""
Cardiac Left Atrial Strain (LAS) & Speckle Tracking Diastolic Mechanics Client.
Zero-mock pure Python standard library implementation.
Calculates LA Reservoir Strain (LASr %), Conduit Strain (LAScd %), Booster/Contraction Strain (LASct %),
Left Atrial Stiffness Index (LASI = (E/e') / LASr), and LV filling pressure / diastolic dysfunction staging.
"""

import math
from typing import Dict, Any, Optional


class LeftAtrialStrainClient:
    """
    Evaluates 2D speckle-tracking left atrial phasic myocardial deformation:
    - Reservoir Strain (LASr %): normal >= 39.0% (< 24.0% indicates elevated LV filling pressures)
    - Conduit Strain (LAScd %): normal 20.0 - 32.0%
    - Booster Pump Strain (LASct %): normal 12.0 - 20.0% (0.0% in atrial fibrillation)
    - LA Stiffness Index (LASI): (E / e') / LASr (normal < 0.22; > 0.35 indicates severe atrial fibrosis)
    - Staged according to ASE/EACVI guidelines for non-invasive diastology and AF recurrence risk.
    """

    def __init__(self):
        pass

    def evaluate_la_strain(
        self,
        reservoir_strain_pct: float,
        booster_pump_strain_pct: Optional[float] = None,
        conduit_strain_pct: Optional[float] = None,
        mitral_e_over_e_prime: Optional[float] = 8.5,
        left_atrial_volume_index_ml_m2: Optional[float] = 28.0,
        rhythm: Optional[str] = "Sinus Rhythm",
        patient_age_years: Optional[int] = 60
    ) -> Dict[str, Any]:
        """
        Calculates left atrial phasic strain and diastolic stiffness.
        reservoir_strain_pct: peak positive strain during LV systole (e.g. 42.0%).
        booster_pump_strain_pct: active strain at atrial contraction (e.g. 15.0%).
        conduit_strain_pct: passive emptying strain (optional, e.g. 27.0%).
        mitral_e_over_e_prime: E/e' ratio (optional, e.g. 8.5).
        """
        if reservoir_strain_pct < 0:
            raise ValueError("Reservoir strain cannot be negative.")

        is_afib = "fibrillation" in rhythm.lower() or "afib" in rhythm.lower()
        if is_afib:
            booster_pump_strain_pct = 0.0

        # Calculate conduit strain if not directly provided: LAScd = LASr - LASct
        if conduit_strain_pct is None and booster_pump_strain_pct is not None:
            conduit_strain_pct = max(0.0, round(reservoir_strain_pct - booster_pump_strain_pct, 1))

        # LA Stiffness Index: (E/e') / LASr
        la_stiffness_index = None
        if mitral_e_over_e_prime and reservoir_strain_pct > 0:
            la_stiffness_index = round(mitral_e_over_e_prime / reservoir_strain_pct, 3)

        # Diastolic Mechanics & Filling Pressure Staging (ASE/EACVI Standards):
        # Normal LASr: >= 35.0% (optimally >= 39.0%)
        # Mildly Impaired: 24.0% - 34.9%
        # Markedly Depressed / Elevated LV Filling Pressures: < 24.0%
        # Severe Atrial Failure: < 18.0%
        if reservoir_strain_pct < 18.0:
            diastolic_status = "Severe LA Myopathy / Markedly Elevated LV Filling Pressures"
            clinical_risk = "Exhausted atrial reservoir compliance and severe LA interstitial fibrosis; high risk of pulmonary hypertension and cardiac decompensation."
        elif reservoir_strain_pct < 24.0:
            diastolic_status = "Depressed LA Reservoir Strain / Elevated Diastolic Filling Pressures"
            clinical_risk = "Elevated left ventricular end-diastolic pressure (LVEDP) transferring chronic wall stress to the left atrium; consistent with Grade II/III diastolic dysfunction or HFpEF."
        elif reservoir_strain_pct < 35.0:
            diastolic_status = "Subclinical LA Reservoir Strain Impairment (Early Diastolic Dysfunction)"
            clinical_risk = "Mild loss of atrial stretching reserve; often paired with compensatory booster pump augmentation in early Grade I relaxation abnormality."
        else:
            diastolic_status = "Normal Physiological Left Atrial Strain (Preserved Compliance)"
            clinical_risk = "Normal left ventricular filling pressures, robust atrial compliance, and low risk of thromboembolism or atrial fibrillation."

        return {
            "status": "success",
            "phasic_strain_metrics": {
                "reservoir_strain_lasr_pct": round(reservoir_strain_pct, 1),
                "conduit_strain_lascd_pct": round(conduit_strain_pct, 1) if conduit_strain_pct is not None else None,
                "booster_pump_strain_lasct_pct": round(booster_pump_strain_pct, 1) if booster_pump_strain_pct is not None else None,
                "la_stiffness_index_lasi": la_stiffness_index,
                "mitral_e_over_e_prime": mitral_e_over_e_prime,
                "la_volume_index_ml_per_m2": left_atrial_volume_index_ml_m2
            },
            "clinical_context": {
                "cardiac_rhythm": rhythm,
                "normal_lasr_lower_limit_pct": 35.0,
                "elevated_filling_pressure_cutoff_pct": 24.0,
                "patient_age_years": patient_age_years
            },
            "cardiac_assessment": {
                "diastolic_status": diastolic_status,
                "pathophysiology_summary": clinical_risk
            }
        }
