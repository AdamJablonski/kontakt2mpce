# MPC Expansion Pack Creation Guide

This document provides a practical guide for creating MPC expansion packs, including MPCe Expressive Kits.

## Overview

An MPC Expansion Pack (.xpn) is a packaged collection of:
- Program files (.xpm)
- Audio samples (.wav)
- Preview files (audio)
- Metadata (Expansion.xml)
- Artwork (image)

## Prerequisites

### Software Requirements

- **MPC Software** (v2.0 or higher)
  - Desktop version for creating and editing programs
  - Includes Expansion Builder utility
  - Free download from Akai Professional website

- **For MPCe Features**:
  - MPC Software v2.11 or higher (for OS 3.6+ compatibility)
  - MPC Live 3 or MPC XL hardware for testing

### Sample Requirements

- **Format**: WAV (uncompressed PCM)
- **Bit Depth**: 16-bit or 24-bit
- **Sample Rate**: 44.1kHz (preferred) or 48kHz
- **Channels**: Mono or Stereo

## Expansion Pack Structure

### Directory Layout

```
MyExpansion/
├── Expansion.xml          # Required: Metadata
├── Artwork.jpg            # Required: Cover image
├── Samples/               # Required: Audio samples
│   ├── Kick_01.wav
│   ├── Snare_01.wav
│   └── ...
├── Programs/              # Required: Program files
│   ├── Kit_01.xpm
│   ├── Kit_02.xpm
│   └── ...
└── Previews/              # Optional: Audio previews
    ├── Kit_01.mp3
    └── Kit_02.mp3
```

### Folder Descriptions

#### Samples/
- Contains all WAV audio files
- Can use subdirectories for organization (e.g., Samples/Kicks/, Samples/Snares/)
- Keep organized for easy reference
- Ensure file names don't contain special characters

#### Programs/
- Contains .xpm program files
- Each file represents one kit or instrument
- XPM files reference samples via relative paths

#### Previews/
- Short audio clips for browser previews
- Name must match corresponding XPM (e.g., Kit_01.xpm → Kit_01.mp3)
- Recommended length: 5-15 seconds
- Can be MP3 or WAV
- Optional but highly recommended

#### Expansion.xml
- Metadata file describing the expansion
- See example below

#### Artwork
- JPG or PNG format
- Recommended size: 512x512 pixels or larger
- Square aspect ratio recommended
- Displayed in expansion browser

## Step-by-Step Creation Process

### Step 1: Prepare Your Samples

1. **Collect or Record Audio**
   - Source or create your drum samples
   - Ensure consistent sample rate (44.1kHz recommended)
   - Normalize levels for consistency

2. **Organize Files**
   ```
   Samples/
   ├── Kicks/
   │   ├── Kick_01.wav
   │   ├── Kick_02.wav
   │   └── ...
   ├── Snares/
   │   ├── Snare_01.wav
   │   ├── Snare_02.wav
   │   └── ...
   └── ...
   ```

3. **For MPCe Expressive Kits**
   - Create 4 variations per sound
   - Name them clearly (e.g., Kick_TL.wav, Kick_TR.wav, Kick_BL.wav, Kick_BR.wav)
   - Ensure variations have distinct characteristics but blend well

### Step 2: Create Programs in MPC Software

1. **Launch MPC Software**
   - Open MPC Software (Desktop mode)

2. **Create New Program**
   - Click "+" in browser
   - Select "Program" → "Drum Program"

3. **Load Samples to Pads**
   - Drag samples from browser to pads
   - Or use Sample Assign mode
   - Assign one sample per pad (basic) or up to 4 layers (MPCe)

4. **Configure Pad Parameters**
   - Tune each pad as needed
   - Set levels and panning
   - Configure filters and envelopes
   - Assign pad colors for visual organization

5. **For MPCe Multi-Layer Pads**
   - Select a pad
   - Go to Pad → Sample Layers
   - Add up to 4 samples per pad
   - Configure layer blending:
     - Velocity-based switching
     - Corner-based (X/Y position)
     - Crossfade settings

6. **Configure Expressive Controls** (MPCe)
   - Go to Pad → Expressive Control
   - Enable X/Y position mapping
   - Assign X-axis parameter (e.g., filter, pitch)
   - Assign Y-axis parameter
   - Set modulation amounts

7. **Save Program**
   - File → Save Program
   - Give it a descriptive name
   - Save to Programs/ folder

8. **Repeat for Additional Programs**
   - Create multiple kits/variations
   - Each saved as separate .xpm file

### Step 3: Create Previews

1. **Create Preview Audio**
   - Record a short performance of each kit
   - 5-15 seconds recommended
   - Showcase the sound and expressive features
   - Export as MP3 or WAV

2. **Name Previews Correctly**
   - Must match XPM filename exactly
   - Example: Kit_01.xpm → Kit_01.mp3

3. **Place in Previews/ Folder**

### Step 4: Create Artwork

1. **Design Cover Image**
   - 512x512 pixels minimum (1024x1024 recommended)
   - Square aspect ratio
   - JPG or PNG format
   - Represents your expansion visually

2. **Save to Root Folder**
   - Save as Artwork.jpg or Artwork.png

### Step 5: Create Expansion.xml

Create metadata file describing your expansion:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Expansion>
  <Identifier>com.yourname.expansionname</Identifier>
  <Title>My MPCe Drum Kit</Title>
  <Manufacturer>Your Name/Brand</Manufacturer>
  <Version>1.0</Version>
  <Description>Collection of expressive drum kits with multi-layered samples optimized for MPC Live 3</Description>
  <Artwork>Artwork.jpg</Artwork>
  <Category>Drums</Category>
  <Keywords>drums, mpce, expressive, 808, acoustic</Keywords>
  <Website>https://yourwebsite.com</Website>
  <ReleaseDate>2026-01-31</ReleaseDate>
</Expansion>
```

#### Metadata Fields

- **Identifier**: Unique ID (reverse-domain style recommended)
- **Title**: Display name (shown in browser)
- **Manufacturer**: Your name or brand
- **Version**: Version number (1.0, 1.1, etc.)
- **Description**: Brief description of contents
- **Artwork**: Filename of cover image
- **Category**: Main category (Drums, Bass, Keys, etc.)
- **Keywords**: Search keywords (comma-separated)
- **Website**: Optional website URL
- **ReleaseDate**: Optional release date (YYYY-MM-DD)

### Step 6: Build Expansion Pack with Expansion Builder

1. **Launch Expansion Builder**
   - Included with MPC Software
   - Find in MPC Software installation folder or application menu

2. **Create New Expansion**
   - File → New Expansion

3. **Select Source Folder**
   - Choose your MyExpansion/ folder
   - Builder will scan for Expansion.xml and content

4. **Verify Content**
   - Check that all programs, samples, and previews are detected
   - Review any warnings or errors

5. **Configure Build Settings**
   - Set output location
   - Choose .xpn filename

6. **Build Expansion**
   - Click "Build" or "Export"
   - Wait for build process to complete
   - Result: MyExpansion.xpn file

### Step 7: Test the Expansion

#### Test in MPC Software (Desktop)

1. **Install Expansion**
   - Drag .xpn file onto MPC Software
   - Or File → Import Expansion

2. **Load Programs**
   - Browse to expansion in browser
   - Load programs and test sounds
   - Verify all samples load correctly

3. **Test Functionality**
   - Play pads and check sound
   - Test velocity response
   - Verify parameters (filters, envelopes, etc.)

#### Test on Hardware (MPC Live 3)

1. **Transfer to Device**
   - Copy .xpn to USB drive or SD card
   - Or use MPC Software to sync to connected device

2. **Install on Hardware**
   - Standalone mode: Go to Menu → Expansion Manager
   - Select expansion and install

3. **Test Expressive Features**
   - Load MPCe programs
   - Test X/Y position detection on pads
   - Verify layer blending and modulation
   - Check that corner mapping works correctly

4. **Performance Test**
   - Play full performance
   - Check CPU usage
   - Verify no dropouts or glitches

### Step 8: Finalize and Distribute

1. **Create Documentation**
   - Write README with kit information
   - List included programs
   - Describe any special features or techniques

2. **Create Demo Video/Audio** (Optional)
   - Showcase the expansion
   - Demonstrate expressive features
   - Upload to YouTube or SoundCloud

3. **Distribution**
   - Share .xpn file via download link
   - Upload to sound libraries or marketplaces
   - Share on MPC community forums

## MPCe-Specific Workflow

### Creating MPCe Expressive Kits

#### Multi-Layer Sample Preparation

1. **Record Variations**
   For each sound, record 4 distinct variations:
   - **Top-Left**: Soft attack, darker timbre
   - **Top-Right**: Soft attack, brighter timbre
   - **Bottom-Left**: Hard attack, darker timbre
   - **Bottom-Right**: Hard attack, brighter timbre

2. **Level Matching**
   - Normalize all variations to similar peak levels
   - Ensures smooth blending when morphing
   - Use gentle compression if needed for consistency

3. **Tonal Variation**
   - EQ variations for tonal differences
   - Filter variations for brightness control
   - Consider mic position or playing technique variations

#### Configuring Expressive Pads

1. **In MPC Software**
   - Load all 4 samples to a single pad
   - Go to Pad → Sample Layers
   - Assign corner positions:
     - Layer 1 → Top-Left
     - Layer 2 → Top-Right
     - Layer 3 → Bottom-Left
     - Layer 4 → Bottom-Right

2. **Set Blend Mode**
   - Crossfade (smooth morphing)
   - Switch (hard transitions)
   - Velocity + Position (hybrid)

3. **Configure Modulation**
   - X-axis: Filter cutoff or sample selection
   - Y-axis: Pitch or envelope
   - Set modulation depth appropriately
   - Test on hardware for feel

4. **Fine-Tune Response**
   - Adjust velocity curves
   - Set layer volume balance
   - Configure filter envelopes
   - Test extensively on MPCe hardware

#### Naming Conventions for MPCe Kits

Clear naming helps users understand content:

```
MyExpansion_MPCe/
├── Programs/
│   ├── 01_Acoustic_MPCe.xpm
│   ├── 02_Electronic_MPCe.xpm
│   └── 03_Hybrid_MPCe.xpm
└── Samples/
    ├── Kicks/
    │   ├── AcKick_TL.wav  (Top-Left)
    │   ├── AcKick_TR.wav  (Top-Right)
    │   ├── AcKick_BL.wav  (Bottom-Left)
    │   └── AcKick_BR.wav  (Bottom-Right)
    └── ...
```

## Tips and Best Practices

### General Tips

1. **Keep It Organized**
   - Use clear folder structure
   - Name files descriptively
   - Document your process

2. **Optimize File Sizes**
   - Trim silence from samples
   - Consider 16-bit for smaller files if quality permits
   - Remove unused samples before packaging

3. **Test Thoroughly**
   - Test on target hardware
   - Check all pads and layers
   - Verify sample paths are correct

4. **Version Control**
   - Keep source files separate from build
   - Maintain backup of pre-build folder
   - Document changes in version notes

### Audio Quality Tips

1. **Sample Preparation**
   - High-quality source material
   - Proper gain staging
   - Minimal processing if possible

2. **Level Consistency**
   - Match levels across similar sounds
   - Leave headroom for mixing
   - Avoid clipping

3. **Format Consistency**
   - Use same sample rate throughout
   - Stick to 16 or 24-bit consistently
   - Mono for mono sounds, stereo for stereo

### MPCe-Specific Tips

1. **Layer Design**
   - Ensure variations are musically useful
   - Test blending between all corners
   - Avoid abrupt jumps in timbre

2. **Expressive Mapping**
   - Don't over-modulate
   - Map parameters that make musical sense
   - Consider performance ergonomics

3. **Hardware Testing**
   - Always test on actual MPCe hardware
   - Software preview may not reflect hardware behavior
   - Adjust based on physical feel

4. **Graceful Degradation**
   - Ensure kit sounds good even without expressive control
   - Layer 1 should be usable standalone
   - Test on non-MPCe hardware for compatibility

## Common Issues and Solutions

### Issue: Samples Not Loading

**Cause**: Incorrect file paths in XPM

**Solution**:
- Use relative paths (e.g., `Samples/Kick.wav`)
- Ensure folder structure matches XPM references
- Check for case sensitivity issues

### Issue: Previews Not Appearing

**Cause**: Preview filename doesn't match XPM filename

**Solution**:
- Ensure exact name match (excluding extension)
- Example: `Kit_01.xpm` requires `Kit_01.mp3`

### Issue: Expansion Won't Build

**Cause**: Missing or invalid Expansion.xml

**Solution**:
- Verify XML syntax
- Ensure all required fields are present
- Check for special characters in identifier

### Issue: MPCe Features Not Working

**Cause**: Hardware doesn't support MPCe or incorrect configuration

**Solution**:
- Test on MPC Live 3 or MPC XL hardware
- Update to MPC OS 3.6 or higher
- Verify expressive control is enabled in program

### Issue: Layer Blending Sounds Wrong

**Cause**: Level mismatch between layers or incorrect blend settings

**Solution**:
- Normalize all layer samples to similar levels
- Adjust blend curve in software
- Test different blend modes

## Manual Installation (Without .xpn)

If you have loose files (not packaged as .xpn):

### Software Mode
1. Copy Programs/ folder contents to MPC's program library
2. Copy Samples/ to accessible location
3. Load programs from browser

### Standalone Mode
1. Copy entire folder structure to SD/USB
2. Navigate to location in browser
3. Load programs directly

## Advanced: Hand-Editing XPM Files

XPM files are XML and can be edited in text editor:

1. **Open in Text Editor**
   - Use any text editor
   - Notepad++, VS Code, or similar recommended

2. **Edit Carefully**
   - Maintain XML structure
   - Don't break closing tags
   - Save as UTF-8 encoding

3. **Common Edits**
   - Change sample paths
   - Adjust parameter values
   - Modify MIDI note assignments

4. **Validate**
   - Test in MPC Software after editing
   - Check for XML syntax errors
   - Verify changes work as expected

**Warning**: Hand-editing can break programs if done incorrectly. Always keep backups.

## Resources

### Official Resources
- [Akai Professional Support](https://support.akaipro.com)
- [MPC Software Downloads](https://www.akaipro.com/downloads)
- [MPC Firmware Updates](https://www.akaipro.com/downloads-and-support/downloads/firmware/mpc/)

### Community Resources
- [MPC Forums](https://www.mpc-forums.com)
- [MPC Samples](https://www.mpc-samples.com)
- [MPC Tutor](https://www.mpc-tutor.com)

### Tutorials
- Official Akai YouTube channel for video tutorials
- Community tutorials on expansion creation
- MPCe-specific feature demonstrations

## Conclusion

Creating MPC expansion packs requires attention to detail but follows a straightforward process:

1. Prepare quality samples
2. Create programs in MPC Software
3. Add metadata and artwork
4. Build with Expansion Builder
5. Test thoroughly
6. Distribute

For MPCe Expressive Kits, the key additions are:
- Multi-layer sample preparation
- Corner-based layer assignment
- Expressive control configuration
- Hardware testing on MPCe devices

Follow this guide and best practices to create professional-quality expansions that work reliably across the MPC ecosystem.
