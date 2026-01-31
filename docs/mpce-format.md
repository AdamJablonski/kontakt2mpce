# MPCe File Format Documentation

## Overview

This document describes the MPCe file format and related structures used in the Akai MPC Live 3. It is based on research from official documentation, tutorials, forum posts, and community resources.

## Important Clarification: MPCe as Hardware vs. File Format

**MPCe** primarily refers to the **hardware technology** in the Akai MPC Live 3, not a distinct file format. Specifically:

- **MPCe Pads**: 3D-sensing, ultra-expressive MPC pad technology with X/Y position detection
- **MPCe Expressive Kits**: Content packs designed to leverage the expressive hardware capabilities
- **File Format**: MPCe Expressive Kits use the standard **XPM** (eXtensible Program Module) format with enhancements for multi-layered samples

The innovation is centered on hardware expressivity and how kits are mapped to pads, not on a fundamentally new file structure.

## MPCe Hardware Features

### 3D-Sensing Pads

The MPCe pads in MPC Live 3 provide:

- **X/Y Position Detection**: Each pad detects finger position across its surface
- **Multi-dimensional Expression**: Beyond velocity and aftertouch
- **Real-time Modulation**: X/Y position can control effects, filters, pitch, sample start/end
- **Dynamic Note Repeat**: Position affects note repeat rate and articulation

### Multi-Layer Architecture

- **Up to 4 sample layers per pad**: Different samples can be mapped to pad "corners"
- **64 total samples instantly available**: 16 pads × 4 layers
- **Seamless Blending**: Corner samples fade into each other for smooth transitions
- **Velocity Switching**: Layers can respond to different velocity ranges

### Control Mapping

X/Y pad movement can be assigned to:
- Filter cutoff and resonance
- Pitch bend and modulation
- Sample start/end points
- Effect parameters
- Articulation switching

## File Format: XPM (eXtensible Program Module)

MPCe Expressive Kits use the standard **XPM** format, which is the modern program format for Akai MPC devices.

### XPM Format Overview

- **File Extension**: `.xpm`
- **Format Type**: XML (plain text, human-readable)
- **Encoding**: UTF-8
- **Compatibility**: MPC Live, MPC X, MPC One, MPC Studio, MPC Renaissance, MPC Beats
- **OS Requirement**: MPC OS 2.x and above (MPCe features require OS 3.6+)

### XPM vs. Legacy PGM Format

| Feature | .pgm (Legacy) | .xpm (Modern) |
|---------|--------------|---------------|
| Format | Binary | XML/Text |
| Max Pads | 16-64 | 128 (8 banks of 16) |
| Layers per Pad | 1 | 4 |
| Devices | MPC2000, MPC1000, MPC2500 | Modern MPCs |
| Velocity Layers | Limited | Full support |
| Sample Path | Filename only | Full path |
| Pad Colors | No | Yes |
| Expressive Control | No | Yes (MPCe) |

### XPM File Structure

#### Basic XML Structure

```xml
<?xml version="1.0" encoding="utf-8"?>
<MPCProgram Name="MyKit" ProgramType="DRUM">
  <NoteAssignments>
    <Pad PadNoteNumber="36" PadIndex="0" PadName="Kick">
      <Samples>
        <Sample SamplePath="Samples/808_Kick_01.wav" Layer="1"/>
      </Samples>
      <Amp EnvelopeAttack="0.00" EnvelopeDecay="0.00"/>
      <Filter Type="LP" Cutoff="120" Resonance="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Pan Value="0"/>
      <Level Value="100"/>
    </Pad>
    <!-- Additional pads... -->
  </NoteAssignments>
</MPCProgram>
```

#### Program Types

- **DRUM**: Standard drum kit (most common)
- **KEYGROUP**: Chromatic/melodic instrument
- **PLUGIN**: VST/AU plugin reference
- **MIDI**: MIDI control program

### MPCe-Specific XPM Features

For MPCe Expressive Kits, the XPM format includes:

#### Multi-Layer Sample Assignment

```xml
<Pad PadNoteNumber="36" PadIndex="0" PadName="Expressive Kick">
  <Samples>
    <Sample SamplePath="Samples/Kick_TL.wav" Layer="1" Corner="TopLeft"/>
    <Sample SamplePath="Samples/Kick_TR.wav" Layer="2" Corner="TopRight"/>
    <Sample SamplePath="Samples/Kick_BL.wav" Layer="3" Corner="BottomLeft"/>
    <Sample SamplePath="Samples/Kick_BR.wav" Layer="4" Corner="BottomRight"/>
  </Samples>
  <ExpressiveControl>
    <XYMapping Enabled="true"/>
    <BlendMode Type="Crossfade"/>
  </ExpressiveControl>
</Pad>
```

#### Expressive Control Parameters

- **X/Y Position Mapping**: Controls which layer(s) are triggered
- **Blend Mode**: How layers mix (crossfade, switch, layer)
- **Modulation Assignments**: X/Y to filter, pitch, effects
- **Velocity Curves**: Per-layer velocity response

### Key XPM Elements

#### Pad Element

```xml
<Pad PadNoteNumber="36" PadIndex="0" PadName="Sample Name">
```

- **PadNoteNumber**: MIDI note (36 = C1, typical for Pad A01)
- **PadIndex**: Pad position (0-127)
- **PadName**: Display name in MPC

#### Sample Element

```xml
<Sample SamplePath="Samples/808_Kick_01.wav" Layer="1"/>
```

- **SamplePath**: Relative or absolute path to WAV file
- **Layer**: Layer number (1-4)
- **VelocityRange**: Optional velocity range for this layer

#### Parameter Elements

Common parameters in XPM files:

- **Amp**: Volume envelope (Attack, Decay, Sustain, Release)
- **Filter**: Type (LP, HP, BP), Cutoff, Resonance
- **Tuning**: Coarse (semitones), Fine (cents)
- **Pan**: Left/Right position
- **Level**: Overall volume
- **MuteGroup**: For hi-hat exclusion groups
- **PadColor**: RGB color for pad display

## Expansion Pack Format (.xpn)

MPCe Expressive Kits are distributed as expansion packs using the `.xpn` format.

### XPN Structure

An XPN file is a compressed archive containing:

```
MyExpansion.xpn/
├── Expansion.xml          # Metadata
├── Artwork.jpg/png        # Cover image
├── Samples/               # WAV files
│   ├── Kick_01.wav
│   ├── Snare_01.wav
│   └── ...
├── Programs/              # XPM files
│   ├── Kit_01.xpm
│   ├── Kit_02.xpm
│   └── ...
└── Previews/              # Audio previews
    ├── Kit_01.mp3
    └── Kit_02.mp3
```

### Expansion.xml Metadata

```xml
<?xml version="1.0" encoding="utf-8"?>
<Expansion>
  <Identifier>com.manufacturer.expansionname</Identifier>
  <Title>My MPCe Kit</Title>
  <Manufacturer>Your Brand</Manufacturer>
  <Version>1.0</Version>
  <Description>MPCe Expressive Kit with multi-layered samples</Description>
  <Artwork>Artwork.jpg</Artwork>
  <Category>Drums</Category>
</Expansion>
```

### Directory Structure Details

#### Samples/

- **Format**: WAV
- **Bit Depth**: 16 or 24-bit recommended
- **Sample Rate**: 44.1kHz standard (48kHz supported but 44.1kHz preferred)
- **Naming**: Clear, descriptive names without special characters
- **Organization**: Can use subdirectories (e.g., Samples/Kicks/, Samples/Snares/)

#### Programs/

- Contains `.xpm` files
- Each XPM references samples via relative paths
- Multiple programs can share the same sample pool

#### Previews/

- Short audio clips (MP3 or WAV)
- Named identically to corresponding XPM file (e.g., Kit_01.mp3 for Kit_01.xpm)
- Used for auditioning in browser without loading full program

### Creating XPN Files

XPN files are created using the **Akai MPC Expansion Builder** utility:

1. Organize content in proper folder structure
2. Open Expansion Builder
3. Select folder containing expansion content
4. Fill in metadata (title, identifier, version, description)
5. Add artwork
6. Build/export to create .xpn file

### Installing XPN Expansions

#### Software (MPC 2.x Desktop)
- Drag and drop .xpn file onto MPC software
- Or use File → Import Expansion

#### Hardware (Standalone Mode)
1. Download expansion via inMusic Software Center
2. Copy to device's Expansions folder (internal drive, SD, or USB)
3. Access via browser in MPC

## Sample Specifications

### Audio Format Requirements

| Specification | Value |
|--------------|-------|
| Format | WAV (uncompressed) |
| Bit Depth | 16 or 24-bit |
| Sample Rate | 44.1kHz (preferred) or 48kHz |
| Channels | Mono or Stereo |
| Encoding | PCM |

### Naming Conventions

- Use clear, descriptive names
- Avoid special characters: `/ \ : * ? " < > |`
- Use underscores or hyphens for spaces
- Include variation info in name (e.g., Kick_Soft.wav, Kick_Hard.wav)

### MPCe Layer Organization

For expressive kits with corner mapping:

- **Layer 1 (Top-Left)**: Often softer/darker variation
- **Layer 2 (Top-Right)**: Often brighter variation
- **Layer 3 (Bottom-Left)**: Often mid-range variation
- **Layer 4 (Bottom-Right)**: Often harder/accent variation

Example naming:
- `Kick_TL.wav` (Top-Left)
- `Kick_TR.wav` (Top-Right)
- `Kick_BL.wav` (Bottom-Left)
- `Kick_BR.wav` (Bottom-Right)

## MIDI Note Mapping

Standard MPC pad layout (MIDI note numbers):

### Bank A (Pads A01-A16)

```
A13(48) A14(49) A15(50) A16(51)
A09(44) A10(45) A11(46) A12(47)
A05(40) A06(41) A07(42) A08(43)
A01(36) A02(37) A03(38) A04(39)
```

### Extended Banks

- **Bank B**: MIDI notes 52-67
- **Bank C**: MIDI notes 68-83
- **Bank D**: MIDI notes 84-99
- **Banks E-H**: Continue sequentially

## Software Requirements

### MPC Operating System

- **Minimum**: MPC OS 2.0 for basic XPM support
- **MPCe Features**: MPC OS 3.6 or higher
- **Latest**: MPC OS 3.7+ for full expressive control integration

### Compatible Devices

#### Full MPCe Support (3D-Sensing Pads)
- **MPC Live III** (primary MPCe device)
- **MPC XL** (with MPCe pads)

#### XPM Format Support (without MPCe hardware)
- MPC Live, MPC Live II
- MPC X, MPC Touch
- MPC One, MPC One+
- MPC Studio
- MPC Renaissance
- MPC Beats (software)

## Creating MPCe Custom Kits

### Workflow

1. **Prepare Samples**: Record or source 4 variations per sound
2. **Organize Files**: Create Samples/ folder with clear naming
3. **Create XPM**: Use MPC software to map samples to pads
4. **Configure Layers**: Assign corner mappings for each pad
5. **Set Expressive Parameters**: Configure X/Y modulation
6. **Test**: Load on MPC Live 3 hardware and test pad response
7. **Package**: Use Expansion Builder to create .xpn

### Tips for Expressive Kits

- **Variation is Key**: Ensure each layer has distinct characteristics
- **Smooth Transitions**: Layers should blend well when crossfaded
- **Consistent Levels**: Match volume across layers for smooth morphing
- **Complementary Timbres**: Choose variations that work together musically
- **Test on Hardware**: Expressive features only fully work on MPCe-equipped hardware

## Compatibility Notes

### Forward Compatibility

- Standard XPM files work on all modern MPCs
- MPCe-enhanced XPM files gracefully degrade on non-MPCe hardware
- On non-MPCe devices, only Layer 1 may trigger, or layers respond to velocity only

### Backward Compatibility

- XPM files can be exported as .pgm for legacy MPC compatibility
- Multi-layer information is lost in .pgm conversion
- 44.1kHz samples ensure best compatibility across all devices

### Cross-Platform

- XPM files work in both MPC Software (desktop) and Standalone mode
- Sample paths should be relative for portability
- Keep expansions on fast media (internal drive or SSD) for best performance

## Technical Limitations

### Current Limitations

- Maximum 128 pads per program (8 banks of 16)
- Maximum 4 layers per pad
- No official public SDK for third-party XPM generation
- Expressive pad features proprietary to Akai hardware
- No documented binary format specification (XML only)

### File Size Considerations

- Large sample libraries can be several GB
- XPM files themselves are small (typically < 100KB)
- Consider sample bit depth and length for storage constraints
- Use mono samples where stereo is not needed

## References and Sources

### Official Documentation

1. **Akai Professional MPC Live III Product Page**
   - https://www.akaipro.com/mpc-live-3/
   - Hardware specifications and MPCe features

2. **Akai Support - Installing Expansion Packs**
   - https://support.akaipro.com/en/support/solutions/articles/69000873678
   - Official guide for installation

3. **Akai Support - Creating Expansion Packs**
   - https://support.akaipro.com/en/support/solutions/articles/69000857886
   - Official guide for expansion creation

4. **MPC Firmware Downloads**
   - https://www.akaipro.com/downloads-and-support/downloads/firmware/mpc/
   - Latest OS versions and release notes

### Community Resources

5. **MPC-Samples File Compatibility Guide**
   - https://www.mpc-samples.com/article/mpc-file-compatibility-1
   - Comprehensive format compatibility information

6. **Hip Hop Drum Samples - Ultimate Expansion Guide**
   - https://hiphopdrumsamples.com/blogs/hip-hop-producer-blog/how-to-create-and-package-akai-mpc-expansions-the-ultimate-guide
   - Detailed tutorial on creating expansions

7. **MPC-Tutor Complete Guide to Expansion Packs**
   - https://www.mpc-tutor.com/mpc-expansion-packs-complete-guide/
   - Best practices and tips

8. **Chicken Systems Translator - Akai MPC Format Info**
   - http://www.chickensys.com/translator/documentation/formatinfo/akaimpc.html
   - Technical format details

### Video Tutorials

9. **Getting Started with MPC Live III - Creating MPCe Custom Kit**
   - https://www.youtube.com/watch?v=LS_ZHTrlUKk
   - Official Akai tutorial

### Press and Reviews

10. **Synth Magazine - Deep Dive into MPCe Expressive Kits**
    - https://synthmagazine.com/akai-professional-unpacks-the-mpc-live-iii-deep-dive-into-mpce-expressive-kits/

11. **Sound On Sound - Akai Pro MPC Live III Review**
    - https://www.soundonsound.com/news/akai-pro-reveal-mpc-live-iii

12. **Attack Magazine - MPC Live III with 3D Sensing Pads**
    - https://www.attackmagazine.com/news/mpc-live-iii-is-here-with-3d-sensing-pads-step-sequencer/

## Conclusion

The "MPCe format" is best understood as an enhancement to the existing XPM format, designed to take advantage of the MPC Live 3's expressive 3D-sensing pad hardware. While the file format itself remains XPM (XML-based), MPCe Expressive Kits utilize multi-layer sample assignments and X/Y position mapping to create dynamic, expressive instruments.

For developers creating tools like kontakt2mpce, the key is to:

1. Generate valid XPM XML files
2. Support multi-layer sample assignment (up to 4 per pad)
3. Include proper metadata in Expansion.xml
4. Follow sample specifications (44.1kHz, 16/24-bit WAV)
5. Structure expansion packs correctly for .xpn packaging

The format is currently proprietary without a public SDK, but the XML structure is well-documented through community resources and reverse engineering efforts.

## Version History

- **v1.0** (2026-01-31): Initial documentation based on research of official sources, community resources, and technical analysis.
