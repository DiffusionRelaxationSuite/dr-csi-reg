# Spectral MRI Data Processing Pipeline

A comprehensive Python toolkit for converting and processing spectral MRI data between MATLAB (.mat) and NIfTI formats, with advanced registration capabilities.

## 🚀 Quick Start

```bash
# 1. Setup environment
python -m venv .venv
source .venv/bin/activate
pip install scipy nibabel nilearn SimpleITK numpy matplotlib opencv-python

# 2. Convert spectral .mat to NIfTI files
python spectral_mat_to_nifti.py

# 3. Register all spectral files (auto-selects central template)
python nifti_registration_pipeline.py input_dir output_dir

# 4. Convert back to .mat (optional verification)
python spectral_nifti_to_mat.py
```

## 📁 Core Scripts

| Script | Purpose |
|--------|---------|
| [`spectral_mat_to_nifti.py`](DOCUMENTATION.md#spectral_mat_to_niftipy) | .mat → NIfTI conversion |
| [`spectral_nifti_to_mat.py`](DOCUMENTATION.md#spectral_nifti_to_matpy) | NIfTI → .mat conversion |
| [`nifti_registration_pipeline.py`](DOCUMENTATION.md#nifti_registration_pipelinepy) | Generic registration |

## 📖 Documentation

See [DOCUMENTATION.md](DOCUMENTATION.md) for complete usage guide, API reference, and examples.

## 🔧 Data Format

**Input .mat structure:**
```python
{
    'data': (31, 104, 52, 12),        # (spectral_points, x, y, z)
    'Resolution': [[1, 1, 1]],        # [x_res, y_res, z_res] in mm
    'spatial_dim': [[104, 52, 12]]    # Spatial dimensions
}
```

**Output:** 31 individual NIfTI files (`spectral_point_000.nii.gz` ... `spectral_point_030.nii.gz`)

## 🏃‍♂️ Example Workflow

```bash
# Convert spectral data to individual NIfTI files
python spectral_mat_to_nifti.py
# → Creates patient2_nifti_spectral_output/ with 31 files

# Register all files using central file as template
python nifti_registration_pipeline.py \
    patient2_nifti_spectral_output \
    patient2_registration_output \
    --processes 4
# → Creates registered .reg.nii.gz files
```

## 💡 Advanced Usage

**Custom template:**
```bash
python nifti_registration_pipeline.py input_dir output_dir \
    --template custom_template.nii.gz --processes 8
```

**Override resolution:**
```python
from main_mat2nifti_spectral import process_spectral_format
process_spectral_format("data.mat", "output", res=[2.0, 2.0, 3.0])
```

**Batch processing:**
```python
from main_register2template_enhanced import process_directory_registration
results = process_directory_registration("input", None, "output", num_processes=12)
```

## 🎨 Visualizations

The pipeline automatically generates:
- PNG previews of first 5 spectral points
- Orthogonal view visualizations
- Processing metadata and statistics

## ✅ Validation

- **Round-trip accuracy**: 100% data preservation verified
- **Metadata preservation**: Resolution and dimensions maintained
- **Error handling**: Comprehensive validation and reporting
- **Clean architecture**: Modular, testable, well-documented code

## 🚦 Status

- ✅ Spectral data conversion (.mat ↔ NIfTI)
- ✅ Generic registration with auto-template selection
- ✅ Parallel processing and comprehensive logging
- ✅ Round-trip verification and data integrity
- ✅ Clean architecture and documentation

## 📋 Requirements

- Python 3.11+
- Virtual environment recommended
- ~2GB RAM for typical spectral datasets
- SimpleITK, scipy, nibabel, nilearn, numpy

---

*This pipeline provides a complete solution for spectral MRI data processing with modern Python practices, comprehensive error handling, and perfect data preservation.*
