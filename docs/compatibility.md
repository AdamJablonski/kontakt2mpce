# MPC Format Compatibility Reference

This document provides detailed compatibility information for MPC file formats across different devices and software versions.

## File Format Overview

| Format | Extension | Type | Era | Primary Devices |
|--------|-----------|------|-----|-----------------|
| Program (Legacy) | .pgm | Binary | 1990s-2000s | MPC60, MPC2000, MPC1000, MPC2500 |
| Program (Modern) | .xpm | XML | 2010s-present | MPC Live, MPC X, MPC One, MPC Studio |
| Expansion Pack | .xpn | Archive | 2010s-present | Modern MPCs |
| Project | .xpj | XML | 2010s-present | Modern MPCs |
| Sequence | .mid | Standard | Universal | All MPCs |

## Device Compatibility Matrix

### Program Files (.xpm vs .pgm)

| Device | .xpm Support | .pgm Support | MPCe Features | Max Pads | Layers/Pad |
|--------|--------------|--------------|---------------|----------|------------|
| **MPC Live III** | ✅ Full | ✅ Import | ✅ Yes | 128 | 4 |
| **MPC XL** | ✅ Full | ✅ Import | ✅ Yes | 128 | 4 |
| **MPC Live II** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC Live** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC X** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC One/One+** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC Touch** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC Studio** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC Renaissance** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC Beats** | ✅ Full | ✅ Import | ❌ No | 128 | 4 |
| **MPC2500** | ❌ No | ✅ Native | ❌ No | 64 | 1 |
| **MPC1000** | ❌ No | ✅ Native | ❌ No | 64 | 1 |
| **MPC2000XL** | ❌ No | ✅ Native | ❌ No | 32 | 1 |
| **MPC2000** | ❌ No | ✅ Native | ❌ No | 32 | 1 |

### Expansion Pack Support (.xpn)

| Device | .xpn Support | Installation Method | Notes |
|--------|--------------|---------------------|-------|
| MPC Live III | ✅ Full | Software Center, Manual Copy | Full MPCe support |
| MPC XL | ✅ Full | Software Center, Manual Copy | Full MPCe support |
| MPC Live/Live II | ✅ Full | Software Center, Manual Copy | No MPCe features |
| MPC X | ✅ Full | Software Center, Manual Copy | No MPCe features |
| MPC One/One+ | ✅ Full | Software Center, Manual Copy | No MPCe features |
| MPC Touch | ✅ Full | Software Center, Manual Copy | Requires computer |
| MPC Studio | ✅ Full | Software Center, Manual Copy | Requires computer |
| MPC Renaissance | ✅ Full | Software Center, Manual Copy | Requires computer |
| MPC Beats | ✅ Full | Software Center, Manual Copy | Software only |
| Legacy MPCs | ❌ No | N/A | Use .pgm files instead |

## Operating System Requirements

### MPC OS (Standalone Hardware)

| OS Version | Released | Key Features | MPCe Support | Devices |
|------------|----------|--------------|--------------|---------|
| **3.7+** | 2025+ | Enhanced step sequencer, improved Q-Link | ✅ Full | Live III, XL |
| **3.6** | 2024+ | Initial MPCe support | ✅ Basic | Live III, XL |
| **2.11+** | 2023+ | Various improvements | ❌ No | Live II, X, One |
| **2.10** | 2022 | Clip matrix improvements | ❌ No | Live II, X, One |
| **2.9** | 2021 | Performance enhancements | ❌ No | Live II, X, One |
| **2.0-2.8** | 2019-2021 | Core modern features | ❌ No | Live, X, One |

### MPC Software (Desktop)

| Version | Released | Key Features | .xpm Support | .xpn Support |
|---------|----------|--------------|--------------|--------------|
| **2.15+** | 2025+ | MPCe software features | ✅ Yes | ✅ Yes |
| **2.11+** | 2023+ | Improved workflow | ✅ Yes | ✅ Yes |
| **2.10** | 2022 | Enhanced browser | ✅ Yes | ✅ Yes |
| **2.0-2.9** | 2019-2021 | Modern MPC platform | ✅ Yes | ✅ Yes |
| **1.x** | 2016-2019 | Renaissance era | ⚠️ Limited | ❌ No |

## Format Conversion

### .pgm to .xpm

**Akai MPC Software (Automatic)**
1. Open MPC Software
2. File → Open Program → Select .pgm file
3. MPC automatically converts on import
4. File → Save Program → Save as .xpm

**Limitations of Conversion:**
- Single layer only (no multi-layering)
- 16-64 pads maximum (depending on source)
- Some parameters may need adjustment
- Sample paths may need updating

### .xpm to .pgm

**Akai MPC Software (Export)**
1. Open .xpm program in MPC Software
2. File → Export Program → Legacy Format
3. Choose .pgm format
4. Save

**Limitations of Export:**
- Multi-layer information is lost
- Only Layer 1 is exported
- Maximum 64 pads
- Some modern parameters not supported
- Expressive control data removed

### Third-Party Conversion Tools

- **Chicken Systems Translator**: Universal sample format converter
  - Supports MPC, Kontakt, SoundFont, and many others
  - Can convert between .pgm and various formats
  - Limited .xpm support (format is proprietary)

## Sample Format Compatibility

### Audio Specifications

| Device/Software | WAV | AIFF | MP3 | FLAC | Bit Depth | Sample Rate |
|-----------------|-----|------|-----|------|-----------|-------------|
| **Modern MPCs** | ✅ | ✅ | ❌ | ❌ | 16/24-bit | 44.1/48kHz |
| **Legacy MPCs** | ✅ | ✅ | ❌ | ❌ | 16-bit | 44.1kHz |
| **MPC Software** | ✅ | ✅ | ❌ | ❌ | 16/24/32-bit | Up to 96kHz |

**Recommendations:**
- Use **WAV** format for maximum compatibility
- Prefer **44.1kHz** sample rate for universal compatibility
- Use **16-bit** for legacy compatibility, **24-bit** for quality
- Avoid sample rates above 48kHz for hardware devices

### Sample Path Handling

#### Relative Paths (Recommended)
```xml
<Sample SamplePath="Samples/Kick.wav"/>
```
- Works across different systems
- Maintains portability
- Required for .xpn packaging

#### Absolute Paths (Not Recommended)
```xml
<Sample SamplePath="/Users/Username/Music/Samples/Kick.wav"/>
```
- Breaks when moved to different system
- Not portable
- Can cause missing sample issues

## MPCe Feature Compatibility

### Expressive Control Features

| Feature | Live III | XL | Other Modern MPCs | Legacy MPCs |
|---------|----------|-----|-------------------|-------------|
| **3D Pad Sensing** | ✅ Hardware | ✅ Hardware | ❌ No | ❌ No |
| **X/Y Position** | ✅ Hardware | ✅ Hardware | ❌ No | ❌ No |
| **4 Layers/Pad** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Corner Mapping** | ✅ Yes | ✅ Yes | ⚠️ Velocity only | ❌ No |
| **Position Modulation** | ✅ Yes | ✅ Yes | ❌ No | ❌ No |

### Graceful Degradation

When MPCe programs are loaded on non-MPCe hardware:

**4-Layer Pads:**
- Modern non-MPCe devices: Layers respond to velocity only
- Layer 1 (soft) → Low velocity
- Layer 4 (hard) → High velocity

**Corner Mapping:**
- Reverts to velocity switching
- X/Y position data ignored
- Still functional, just less expressive

**Modulation:**
- Position-based modulation disabled
- Standard velocity modulation works
- Envelope and filter settings retained

## Cross-Platform Considerations

### File System Compatibility

| Platform | Case Sensitivity | Path Separator | Max Path Length | Special Characters |
|----------|------------------|----------------|-----------------|-------------------|
| **Windows** | No | `\` or `/` | 260 characters | Avoid: `< > : " / \ | ? *` |
| **macOS** | No (HFS+/APFS) | `/` | 1024 characters | Avoid: `:` (HFS+) |
| **Linux** | Yes | `/` | 4096 characters | Avoid: `/` only |
| **MPC Hardware** | Varies | `/` | Device dependent | Avoid all special chars |

**Best Practices:**
- Use lowercase filenames
- Avoid spaces (use underscores or hyphens)
- Keep paths under 200 characters
- Only use alphanumeric characters, underscores, and hyphens

### Storage Media Compatibility

| Media Type | MPC Live III | Other Standalone MPCs | Speed | Recommendation |
|------------|--------------|----------------------|-------|----------------|
| **Internal SSD** | ✅ Best | ✅ Best | Fastest | ✅ Best for performance |
| **SD Card (UHS-I)** | ✅ Good | ✅ Good | Fast | ✅ Good for portability |
| **SD Card (Class 10)** | ⚠️ OK | ⚠️ OK | Medium | ⚠️ May have latency |
| **SD Card (Class 4)** | ❌ Slow | ❌ Slow | Slow | ❌ Not recommended |
| **USB 3.0 SSD** | ✅ Excellent | ✅ Excellent | Very Fast | ✅ Excellent for large libraries |
| **USB 3.0 HDD** | ⚠️ OK | ⚠️ OK | Medium | ⚠️ OK for backup |
| **USB 2.0** | ⚠️ Slow | ⚠️ Slow | Slow | ❌ Not recommended |

## Import/Export Workflows

### From Kontakt to MPC

**Current State (kontakt2mpce project):**
- Kontakt uses NKI format (proprietary, XML-based)
- Goal: Convert NKI instruments to XPM programs
- Challenges:
  - Different parameter models
  - Different scripting/modulation systems
  - Sample format differences

**Workflow:**
1. Extract sample references from NKI
2. Convert/copy samples to WAV format
3. Map Kontakt zones to MPC pads
4. Convert parameters (envelopes, filters, etc.)
5. Generate XPM file
6. Package as expansion

### From MPC to Other Formats

**To Ableton Live:**
- Export samples
- Manually recreate in Drum Rack
- Or use Sampler instrument

**To Native Instruments Maschine:**
- No direct conversion available
- Manual recreation required
- Samples can be reused

**To Universal Format (SoundFont):**
- Use Chicken Systems Translator
- Converts from .pgm
- Limited parameter translation

## Compatibility Checklist

### For Maximum Compatibility

- [ ] Use .xpm format (not .pgm)
- [ ] WAV samples at 44.1kHz, 16 or 24-bit
- [ ] Relative paths for all sample references
- [ ] File names without special characters
- [ ] Samples and programs in standard folder structure
- [ ] Proper Expansion.xml with valid identifier
- [ ] Test on target hardware/software
- [ ] Include previews for better user experience
- [ ] Document any special requirements
- [ ] Include README with installation instructions

### For MPCe Compatibility

- [ ] Requires MPC Live III or MPC XL hardware
- [ ] MPC OS 3.6 or higher
- [ ] 4 layers assigned to corners (when using corner mapping)
- [ ] Expressive control parameters configured
- [ ] Tested on actual MPCe hardware
- [ ] Graceful degradation tested on non-MPCe devices
- [ ] Documentation mentions MPCe requirements

## Troubleshooting Compatibility Issues

### Issue: Program Loads But No Sound

**Possible Causes:**
- Sample paths broken
- Samples not found
- Sample format not supported

**Solutions:**
- Check sample file locations
- Verify relative paths
- Convert samples to WAV 44.1kHz

### Issue: Some Pads Work, Others Don't

**Possible Causes:**
- Missing samples for specific pads
- Path issues for some samples
- Corrupted XPM file

**Solutions:**
- Open XPM in text editor
- Check all sample paths
- Verify all referenced samples exist

### Issue: MPCe Features Not Working

**Possible Causes:**
- Wrong hardware (non-MPCe device)
- Old firmware
- Expressive control not enabled

**Solutions:**
- Check hardware model (must be Live III or XL)
- Update to MPC OS 3.6+
- Enable expressive control in program settings

### Issue: Layers Not Triggering

**Possible Causes:**
- Velocity ranges don't cover full range
- Corner mapping not set
- Layer samples missing

**Solutions:**
- Check velocity ranges (should cover 1-127)
- Verify corner assignments
- Ensure all layer samples exist

### Issue: Expansion Won't Install

**Possible Causes:**
- Corrupt .xpn file
- Invalid Expansion.xml
- Insufficient storage space
- File system errors

**Solutions:**
- Rebuild .xpn with Expansion Builder
- Validate XML syntax
- Check available storage
- Reformat storage media if needed

## Version Migration

### Upgrading from MPC OS 2.x to 3.x

**What Changes:**
- New features available (MPCe support on compatible hardware)
- Improved browser and workflow
- Better performance

**What Stays Compatible:**
- All .xpm files continue to work
- All .xpn expansions remain compatible
- Samples and projects unaffected

**Recommendations:**
- Backup before upgrading
- Update MPC Software to match OS version
- Read firmware release notes

### Migrating from Legacy MPC

**From MPC1000/2500 to Modern MPC:**

1. **Backup Everything**
   - Copy all .pgm files
   - Copy all samples
   - Document your setup

2. **Convert Programs**
   - Import .pgm into MPC Software
   - Automatically converts to .xpm
   - Verify sample loading

3. **Update Workflow**
   - Learn new 8-bank pad system (vs. 4-bank)
   - Explore multi-layer capabilities
   - Utilize new effects and features

4. **Preserve Legacy Compatibility**
   - Keep original .pgm files as backup
   - Export .pgm from modern MPC if needed for legacy hardware

## Future-Proofing

### Best Practices for Longevity

1. **Use Open Standards Where Possible**
   - WAV for audio (universal format)
   - Standard MIDI note mappings
   - Clear documentation

2. **Maintain Source Files**
   - Keep original samples separate
   - Document your process
   - Version control for projects

3. **Test Across Devices**
   - Test on multiple MPC models
   - Verify in both software and hardware
   - Check compatibility with older OS versions

4. **Document Dependencies**
   - Note required OS version
   - List hardware requirements
   - Specify software version used

5. **Follow Naming Conventions**
   - Consistent, clear naming
   - No special characters
   - Version numbers in filenames

## Conclusion

Understanding MPC format compatibility ensures your expansions and programs work reliably across the ecosystem. Key takeaways:

- **.xpm is the modern standard** - Use it for all new projects
- **MPCe features require specific hardware** - Live III or XL only
- **44.1kHz WAV samples** - Maximum compatibility
- **Relative paths always** - Essential for portability
- **Test on target devices** - Don't assume compatibility

For the kontakt2mpce project, focus on generating valid .xpm files with proper sample references, and package using the standard expansion structure for maximum compatibility across the MPC platform.
