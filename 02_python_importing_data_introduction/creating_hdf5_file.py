import h5py
import numpy as np

filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'

# Open file in 'w' mode (write/overwrite)
with h5py.File(filename, 'w') as f:
    
    # 1. Strain: The actual gravitational wave data
    # Creating a dataset with random noise to simulate the signal
    strain = f.create_group('strain')
    strain.create_dataset('Strain', data=np.random.rand(1000))
    
    # 2. Meta: Metadata about the observatory
    meta = f.create_group('meta')
    meta.create_dataset('Description', data=b'Simulated LIGO data for practice')
    meta.create_dataset('GPSstart', data=815411200)
    
    # 3. Quality: Info regarding data integrity
    quality = f.create_group('quality')
    quality.create_dataset('mask', data=np.ones(1000, dtype=int))

print(f"File '{filename}' created successfully.")