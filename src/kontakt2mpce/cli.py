"""
Command-line interface for kontakt2mpce.
"""

import argparse
import logging
import sys
from pathlib import Path

from kontakt2mpce import __version__


def setup_logging(verbose: bool = False):
    """Configure logging for the application."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Convert Native Instruments Kontakt instruments to Akai MPC Keygroup format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  kontakt2mpce input.nki output/
  kontakt2mpce -v input.nki output/
  kontakt2mpce --version
        """
    )
    
    parser.add_argument(
        'input',
        type=str,
        nargs='?',
        help='Input Kontakt instrument file (.nki)'
    )
    
    parser.add_argument(
        'output',
        type=str,
        nargs='?',
        help='Output directory for MPC files'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'kontakt2mpce {__version__}'
    )
    
    args = parser.parse_args()
    
    # Show help if no arguments provided
    if not args.input:
        parser.print_help()
        return 0
    
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        return 1
    
    if not input_path.suffix.lower() == '.nki':
        logger.error(f"Input file must be a .nki file, got: {input_path.suffix}")
        return 1
    
    # Validate or create output directory
    output_path = Path(args.output) if args.output else input_path.parent / f"{input_path.stem}_mpc"
    output_path.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Converting {input_path} to {output_path}")
    
    try:
        # TODO: Implement actual conversion
        from kontakt2mpce.converter import convert_nki_to_xpm
        convert_nki_to_xpm(input_path, output_path)
        logger.info("Conversion completed successfully!")
        return 0
    except Exception as e:
        logger.error(f"Conversion failed: {e}", exc_info=args.verbose)
        return 1


if __name__ == '__main__':
    sys.exit(main())
