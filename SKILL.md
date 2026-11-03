---
name: genpark-personal-agent-cardiac-left-atrial-strain-speckle-tracking-skill
description: Evaluates 2D speckle-tracking left atrial phasic deformation (reservoir LASr, conduit LAScd, booster pump LASct) and LA stiffness index to stratify left ventricular filling pressures and HFpEF.
---

# Cardiac Left Atrial Strain (LAS) & Speckle Tracking Skill

This skill computes left atrial phasic myocardial deformation parameters from speckle-tracking echocardiography to detect subclinical diastolic dysfunction, elevated left ventricular end-diastolic pressure (LVEDP), and atrial cardiomyopathy according to EACVI/ASE consensus guidelines.

## Core Capabilities
- Evaluates Reservoir Strain ($LASr\%$, normal $\ge 35.0\%$, filling pressure cutoff $< 24.0\%$).
- Evaluates Conduit Strain ($LAScd\%$, normal $20.0 - 32.0\%$).
- Evaluates Booster Pump Contraction Strain ($LASct\%$, normal $12.0 - 20.0\%$, $0.0\%$ in atrial fibrillation).
- Computes Left Atrial Stiffness Index ($LASI = (E/e') / LASr$, normal $< 0.22$).
- Highly sensitive early biomarker for heart failure with preserved ejection fraction (HFpEF).

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
