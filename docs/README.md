# MPCe and MPC Format Documentation

This directory contains comprehensive documentation about the MPCe file format and related MPC formats used in Akai MPC devices, with a focus on the MPC Live 3.

## Documentation Files

### [mpce-format.md](mpce-format.md) - Main Format Documentation
**Start here for a complete overview of the MPCe format.**

This is the primary documentation file covering:
- MPCe hardware features and capabilities
- XPM (eXtensible Program Module) file format
- XML structure and elements
- Expansion pack (.xpn) structure
- Sample specifications
- MIDI note mapping
- Software requirements
- References and sources

### [xpm-examples.md](xpm-examples.md) - XPM File Examples
**Detailed XML examples for different program types.**

Contains practical examples of:
- Basic drum kits
- MPCe expressive kits with multi-layer pads
- Keygroup instruments (melodic)
- Advanced parameter configurations
- Effect settings
- Notes on creating valid XPM files

### [expansion-creation.md](expansion-creation.md) - Expansion Creation Guide
**Step-by-step guide for creating expansion packs.**

Covers the complete workflow:
- Prerequisites and requirements
- Expansion pack structure
- Sample preparation
- Creating programs in MPC software
- Configuring MPCe expressive controls
- Using Expansion Builder
- Testing and distribution
- Common issues and solutions
- Best practices

### [compatibility.md](compatibility.md) - Format Compatibility Reference
**Compatibility information across devices and formats.**

Detailed compatibility tables and information:
- Device compatibility matrix
- Operating system requirements
- Format conversion (.pgm ↔ .xpm)
- Sample format compatibility
- MPCe feature support across devices
- Cross-platform considerations
- Troubleshooting compatibility issues
- Future-proofing strategies

## Quick Start

### For Developers (kontakt2mpce project)

If you're working on the kontakt2mpce converter:

1. **Read** [mpce-format.md](mpce-format.md) - Understand the XPM format and structure
2. **Study** [xpm-examples.md](xpm-examples.md) - See real XML structure examples
3. **Review** [compatibility.md](compatibility.md) - Understand compatibility requirements
4. **Reference** [expansion-creation.md](expansion-creation.md) - Learn packaging workflow

### For Content Creators

If you're creating MPC expansion packs:

1. **Start with** [expansion-creation.md](expansion-creation.md) - Complete workflow guide
2. **Reference** [mpce-format.md](mpce-format.md) - Technical format details
3. **Use** [xpm-examples.md](xpm-examples.md) - Copy and adapt examples
4. **Check** [compatibility.md](compatibility.md) - Ensure compatibility

### For Researchers

If you're researching MPC formats:

1. **Begin with** [mpce-format.md](mpce-format.md) - Comprehensive overview with sources
2. **Deep dive** [compatibility.md](compatibility.md) - Historical format evolution
3. **Analyze** [xpm-examples.md](xpm-examples.md) - Actual format structure

## Key Findings Summary

### MPCe Clarification

**Important**: "MPCe" primarily refers to **hardware technology** (3D-sensing expressive pads), not a unique file format. MPCe Expressive Kits use the standard **XPM format** with enhancements for multi-layer samples and expressive control.

### File Formats

- **.xpm**: Modern XML-based program format (recommended)
- **.pgm**: Legacy binary program format (for compatibility)
- **.xpn**: Expansion pack archive (contains .xpm, samples, metadata)

### Hardware Support

- **MPCe Features**: Only on MPC Live III and MPC XL
- **XPM Format**: All modern MPC devices (2.x software)
- **Multi-layer Pads**: All modern MPCs (expressive control needs MPCe hardware)

### Critical Requirements

1. **Sample Format**: WAV, 44.1kHz, 16 or 24-bit
2. **Paths**: Always use relative paths for portability
3. **Structure**: Follow standard expansion pack folder layout
4. **Metadata**: Valid Expansion.xml required for .xpn
5. **Testing**: Always test on target hardware/software

## Technical Specifications

### XPM Format
- **Type**: XML (plain text)
- **Encoding**: UTF-8
- **Max Pads**: 128 (8 banks of 16)
- **Layers per Pad**: Up to 4
- **Program Types**: DRUM, KEYGROUP, PLUGIN, MIDI

### Sample Specifications
- **Format**: WAV (PCM uncompressed)
- **Bit Depth**: 16 or 24-bit
- **Sample Rate**: 44.1kHz (preferred) or 48kHz
- **Channels**: Mono or Stereo

### Expansion Pack Structure
```
MyExpansion/
├── Expansion.xml          # Metadata
├── Artwork.jpg            # Cover image
├── Samples/               # WAV files
├── Programs/              # XPM files
└── Previews/              # Audio previews
```

## Sources

Documentation compiled from:
- Official Akai Professional documentation
- MPC software release notes
- Community forums (MPC-Forums, MPC-Samples)
- Technical analyses and reverse engineering
- Product reviews and tutorials
- Video demonstrations

See [mpce-format.md](mpce-format.md) for complete reference list with URLs.

## Limitations and Caveats

### Current Limitations

1. **No Official SDK**: Akai has not released a public SDK for XPM generation
2. **Proprietary Format**: XPM structure is documented through observation and community research
3. **MPCe Hardware-Dependent**: Expressive features only work on specific hardware
4. **Format Evolution**: Format may change with software updates

### Documentation Status

This documentation is based on:
- Research conducted: January 2026
- MPC OS version: 3.7+ (current at time of research)
- MPC Software: 2.15+ (current at time of research)

Format details may change with future software updates. Always refer to official Akai documentation for the latest specifications.

## Contributing

This documentation is part of the kontakt2mpce project. If you discover:
- Corrections or updates needed
- Additional format details
- New features in updated software
- Better examples or explanations

Please contribute back to the project.

## Version History

- **v1.0** (2026-01-31): Initial comprehensive documentation
  - Main format documentation (mpce-format.md)
  - XPM examples (xpm-examples.md)
  - Expansion creation guide (expansion-creation.md)
  - Compatibility reference (compatibility.md)

## License

This documentation is provided for educational and development purposes. MPC, MPCe, and related trademarks are property of Akai Professional / inMusic Brands, Inc.

## Related Projects

- **kontakt2mpce**: Converter from Native Instruments Kontakt format to MPC format (parent project)
- **MPC Software**: Official Akai software for MPC devices
- **Chicken Systems Translator**: Third-party sample format converter

## Contact and Resources

- **Akai Professional**: https://www.akaipro.com
- **MPC Support**: https://support.akaipro.com
- **Community Forums**: https://www.mpc-forums.com
- **MPC Samples**: https://www.mpc-samples.com

---

*This documentation was created through extensive research of official sources, community resources, and technical analysis. While comprehensive and accurate to the best of our knowledge, it is not an official specification from Akai Professional.*
