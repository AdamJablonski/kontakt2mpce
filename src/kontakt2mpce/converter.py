"""
Main conversion logic for Kontakt to MPC conversion.
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def convert_nki_to_xpm(input_path: Path, output_path: Path):
    """
    Convert a Kontakt .nki file to MPC .xpm format.
    
    Args:
        input_path: Path to the input .nki file
        output_path: Path to the output directory
        
    Raises:
        NotImplementedError: This is a placeholder implementation
    """
    logger.info(f"Starting conversion: {input_path.name}")
    logger.info(f"Output directory: {output_path}")
    
    # TODO: Implement conversion logic
    # 1. Parse NKI file (using nkitool or direct parsing)
    # 2. Extract sample mappings
    # 3. Convert audio files if needed
    # 4. Generate XPM file
    # 5. Organize output files
    
    raise NotImplementedError(
        "Conversion not yet implemented. "
        "See PLAN.md for implementation roadmap."
    )
