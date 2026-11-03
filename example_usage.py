"""
Example usage for Cardiac Left Atrial Strain (LAS) Skill.
"""

from client import LeftAtrialStrainClient


def main():
    client = LeftAtrialStrainClient()

    print("--- Case 1: Normal Physiological Left Atrial Strain ---")
    normal_case = client.evaluate_la_strain(
        reservoir_strain_pct=41.5,
        booster_pump_strain_pct=16.0,
        mitral_e_over_e_prime=7.8,
        left_atrial_volume_index_ml_m2=26.0,
        patient_age_years=48
    )
    print("Reservoir Strain (LASr):", normal_case["phasic_strain_metrics"]["reservoir_strain_lasr_pct"], "%")
    print("Conduit Strain (LAScd):", normal_case["phasic_strain_metrics"]["conduit_strain_lascd_pct"], "%")
    print("Booster Pump Strain (LASct):", normal_case["phasic_strain_metrics"]["booster_pump_strain_lasct_pct"], "%")
    print("LA Stiffness Index:", normal_case["phasic_strain_metrics"]["la_stiffness_index_lasi"])
    print("Diastolic Status:", normal_case["cardiac_assessment"]["diastolic_status"])
    print("Pathophysiology:", normal_case["cardiac_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Grade II Diastolic Dysfunction / HFpEF (Elevated Filling Pressure) ---")
    hfpef_case = client.evaluate_la_strain(
        reservoir_strain_pct=21.0,
        booster_pump_strain_pct=9.5,
        mitral_e_over_e_prime=14.2,
        left_atrial_volume_index_ml_m2=38.0,
        patient_age_years=72
    )
    print("Reservoir Strain (LASr):", hfpef_case["phasic_strain_metrics"]["reservoir_strain_lasr_pct"], "%")
    print("LA Stiffness Index:", hfpef_case["phasic_strain_metrics"]["la_stiffness_index_lasi"])
    print("Diastolic Status:", hfpef_case["cardiac_assessment"]["diastolic_status"])
    print("Pathophysiology:", hfpef_case["cardiac_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Atrial Fibrillation with Loss of Booster Pump ---")
    afib_case = client.evaluate_la_strain(
        reservoir_strain_pct=16.5,
        rhythm="Atrial Fibrillation",
        mitral_e_over_e_prime=12.0,
        left_atrial_volume_index_ml_m2=44.0,
        patient_age_years=76
    )
    print("Reservoir Strain (LASr):", afib_case["phasic_strain_metrics"]["reservoir_strain_lasr_pct"], "%")
    print("Booster Pump Strain:", afib_case["phasic_strain_metrics"]["booster_pump_strain_lasct_pct"], "%")
    print("Diastolic Status:", afib_case["cardiac_assessment"]["diastolic_status"])


if __name__ == "__main__":
    main()
