# kontakt2mpce

Convert Native Instruments Kontakt 5-8 instruments to Akai MPC Keygroup format.

## Overview

This project aims to convert Kontakt .nki instrument files to Akai MPC .xpm format, focusing on multi-sample mapping and playback functionality. The converter handles sample organization, audio format conversion, and zone mapping to make Kontakt libraries usable on MPC hardware and software.

## Current Status

🚧 **Under Development** - This is an active research and development project.

See [PLAN.md](PLAN.md) for detailed project plan, architecture, and implementation roadmap.

## Features (Planned)

- ✅ Parse Kontakt instrument files (.nki)
- ✅ Extract sample mappings (zones, key ranges, velocity layers)
- ✅ Convert audio formats (AIFF, WAV, NCW)
- ✅ Generate MPC Keygroup files (.xpm)
- ✅ Organize samples in MPC-compatible folder structure
- 📋 Command-line interface
- 📋 Batch conversion support
- 📋 GUI application (future)

## Installation

**Note:** The project is not yet functional. Installation instructions will be added when the MVP is ready.

```bash
# Clone the repository
git clone https://github.com/AdamJablonski/kontakt2mpce.git
cd kontakt2mpce

# Install dependencies
pip install -e .
```

## Usage

**Note:** The converter is not yet implemented. This shows the planned interface.

```bash
# Basic conversion
kontakt2mpce input.nki output_directory/

# Verbose mode
kontakt2mpce -v input.nki output_directory/

# Show help
kontakt2mpce --help
```

## Requirements

- Python 3.8+
- FFmpeg (for audio conversion)
- pydub
- lxml

## Supported Formats

### Input (Kontakt)
- .nki files (Kontakt 1-8)
- WAV, AIFF, NCW sample formats

### Output (MPC)
- .xpm files (MPC X/Live/One/Software)
- WAV samples (organized in folders)

## Limitations

This converter focuses on **basic sample mapping** and does not support:
- Effects and audio routing
- Advanced modulation and envelopes
- Kontakt scripting (KSP)
- Complex round-robin and keyswitch articulations
- Time-stretching and advanced sample manipulation

See [PLAN.md](PLAN.md) for detailed technical limitations.

## Project Background

### Similar Projects

This project is inspired by and references:

- **[ConvertWithMoss](https://www.mossgrabers.de/Software/ConvertWithMoss/)** - Multi-format sampler converter (Java)
- **[nkitool](https://github.com/reales/nkitool)** - Kontakt NKI extraction tool (C)
- **ChickenSys Translator** - Commercial format converter

### Why This Project?

While excellent tools exist, this project aims to:
- Provide an open-source, Python-based solution
- Focus specifically on Kontakt → MPC workflow
- Be easily extensible and maintainable
- Support modern Kontakt versions (5-8)

## Development

See [PLAN.md](PLAN.md) for:
- Detailed architecture
- Implementation phases
- Technical challenges and solutions
- Development timeline

## Contributing

Contributions are welcome! Areas needing help:
- Kontakt 5-8 format reverse engineering
- Testing with various Kontakt libraries
- Documentation and examples
- GUI development (future)

## License

MIT License - See LICENSE file for details.

## Disclaimer

This tool is for legitimate use only. Users must own legal copies of Kontakt instruments they convert. This is a format converter for interoperability, not a piracy tool. Native Instruments, Kontakt, Akai, and MPC are trademarks of their respective owners.
