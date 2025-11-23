
# Imports
from spectral_mat_to_nifti import convert_spectral_mat_to_nifti
from deformation_utils import apply_nonlinear_deformation_to_nifti_files
from nifti_registration_pipeline import register_nifti
from spectral_nifti_to_mat import convert_spectral_nifti_to_mat
import scipy.io as sio


# Input path
input_mat = "/home/ajoshi/Downloads/Phantom_data.mat"  # Path to input .mat file

# Loop over deformation magnitudes
for magnitude in [30, 50, 100]:
	print(f"\n=== Processing deformation magnitude: {magnitude} ===")
	output_dir = f"phantom_nifti_output_def{magnitude}"
	deformed_dir = f"phantom_nifti_deformed_def{magnitude}"

	# Step 1: Convert spectral .mat file to NIFTI format
	print("Converting spectral .mat file to NIFTI format...")
	convert_spectral_mat_to_nifti(input_mat, output_dir)

	# Step 2: Apply nonlinear deformation to NIFTI files
	print("Applying nonlinear deformation to NIFTI files...")
	apply_nonlinear_deformation_to_nifti_files(output_dir, deformed_dir, magnitude_range=[magnitude, magnitude])
	print("Converting deformed NIFTI files back to .mat format...")
	output_mat = f"phantom_deformed_def{magnitude}.mat"
	convert_spectral_nifti_to_mat(deformed_dir, output_mat, original_mat_file=input_mat)

	# Step 3: Register deformed NIFTI files
	print("Registering deformed NIFTI files...")
	registered_dir = deformed_dir + "_registered"
	register_nifti(deformed_dir, registered_dir, processes=1)

	# Step 4: Convert registered NIFTI files back to .mat format
	print("Converting registered NIFTI files back to .mat format...")
	output_mat = f"phantom_registered_def{magnitude}.mat"
	convert_spectral_nifti_to_mat(registered_dir, output_mat, original_mat_file=input_mat)

