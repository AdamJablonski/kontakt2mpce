# Kontakt to MPCe Conversion Project Plan

## Executive Summary

This project aims to convert Native Instruments Kontakt 5-8 instrument files (.nki) to Akai MPC Keygroup format (.xpm), focusing specifically on multi-sample playback functionality. We will skip effects, audio routing, and advanced features to concentrate on core sample mapping and playback.

## Background Research

### Native Instruments Kontakt Format (.nki)

**File Structure:**
- **Proprietary binary format** (with some XML metadata in older versions)
- **Zones:** Individual samples assigned to MIDI key/velocity ranges
- **Groups:** Collections of zones sharing settings (envelopes, filters, effects)
- **Instruments:** Complete configuration including groups, zones, modulation, and scripting
- **Sample References:** Usually external WAV/AIFF/NCW files (or embedded in monolith format)
- **Version Compatibility:** Format changes between Kontakt versions (especially 4.x vs 5.x+)

**Sample Playback:**
- Key/velocity range mapping
- Root note/pitch settings
- Volume/pan settings
- Sample start/end/loop points
- Round-robin and keyswitching (for advanced articulations)

**Audio Formats:**
- WAV (uncompressed PCM)
- AIFF (uncompressed)
- NCW (Native Compressed Wave - proprietary lossless compression)

### Akai MPC Keygroup Format (.xpm)

**File Structure:**
- **XML-based text format** (human-readable and editable)
- **Zones:** Sample mappings with key/velocity ranges
- **Programs:** Can be DRUM, KEYGROUP, PLUGIN, or MIDI types
- **External Sample References:** References WAV files (typically in relative paths)
- **No Effects/Routing:** Focus on sample playback mapping

**Sample Playback:**
```xml
<Zones>
    <Zone>
        <Sample>Samples/Piano_C2.wav</Sample>
        <Root>60</Root>           <!-- MIDI note number -->
        <LowKey>60</LowKey>       <!-- Lowest key in range -->
        <HighKey>60</HighKey>     <!-- Highest key in range -->
        <LowVel>1</LowVel>        <!-- Lowest velocity -->
        <HighVel>127</HighVel>    <!-- Highest velocity -->
        <Tuning>0</Tuning>        <!-- Fine tuning -->
        <Volume>0</Volume>        <!-- Volume adjustment -->
        <Pan>0</Pan>              <!-- Pan position -->
        <!-- Additional parameters... -->
    </Zone>
</Zones>
```

**Distribution:**
- Individual .xpm + WAV files in folder structure
- Can be packaged as .xpn for easy installation

### SFZ Format (Intermediate/Reference)

**Why SFZ matters:**
- Open, text-based format similar to XPM
- Well-documented with extensive community support
- Can serve as intermediate format for validation
- Tools like `nkitool` can extract NKI to SFZ

**Structure:**
```
<group> group=1
<region> sample=Piano_C2.wav lokey=60 hikey=60 pitch_keycenter=60 lovel=1 hivel=127
```

## Similar Existing Projects

### 1. ConvertWithMoss (Primary Reference)
- **URL:** https://www.mossgrabers.de/Software/ConvertWithMoss/
- **License:** Free, open-source
- **Language:** Java
- **Platforms:** Windows, macOS, Linux
- **Capabilities:**
  - Reads: Kontakt 1-7 (best support for 4.2 and earlier), Bitwig, SFZ, SF2, WAV, and more
  - Writes: Akai MPC Keygroups (.xpm), Bitwig, SFZ, SF2, and more
  - Handles multi-sample mapping
  - Bulk conversion of folders
- **Limitations:**
  - Limited support for newer Kontakt formats (5-8)
  - Does not preserve advanced scripting or complex modulation
  - Commercial Kontakt libraries with heavy scripting may not convert perfectly
- **Learning Opportunity:** Study source code for format conversion logic

### 2. nkitool
- **URL:** https://github.com/reales/nkitool
- **License:** Open-source
- **Language:** C
- **Capabilities:**
  - Extracts samples, metadata from Kontakt v1-4 NKI files
  - Creates SFZ instrument files
  - Extracts XML metadata
  - Handles compressed samples
- **Limitations:**
  - Only supports Kontakt v1-4 (not 5-8)
  - Command-line tool, not a library
  - Requires external tools for audio format conversion
- **Usage:** Can be wrapped by Python using subprocess

### 3. ChickenSys Translator
- **URL:** https://chickensys.com/translator/
- **License:** Commercial ($150-200)
- **Capabilities:**
  - Cross-format sampler conversion
  - Kontakt to various formats including MPC
- **Limitations:**
  - Closed-source, paid
  - Mixed reports on conversion quality for MPC
- **Relevance:** Reference for understanding what's possible

## Python Libraries and Tools

### Audio Format Conversion

**1. PyDub (Recommended for format conversion)**
```python
from pydub import AudioSegment
audio = AudioSegment.from_file("input.aiff")
audio.export("output.wav", format="wav")
```
- **Dependencies:** FFmpeg (must be installed separately)
- **Formats:** WAV, AIFF, MP3, OGG, FLAC, etc.
- **Pros:** High-level API, easy to use
- **Cons:** Requires FFmpeg installation

**2. soundfile + wavio**
```python
import soundfile as sf
import wavio

data, samplerate = sf.read('input.aiff')
wavio.write('output.wav', data, samplerate, sampwidth=2)
```
- **Dependencies:** libsndfile
- **Formats:** WAV, AIFF (via libsndfile)
- **Pros:** Pure Python, efficient
- **Cons:** Limited to uncompressed formats

**3. Standard Library (wave)**
```python
import wave
```
- **Formats:** WAV only
- **Pros:** No dependencies
- **Cons:** Very basic functionality

**Note on NCW:** Native Compressed Wave format is proprietary and DRM-locked. Must be converted to WAV/AIFF using Kontakt before processing in Python.

### XML Processing

**1. xml.etree.ElementTree (Standard Library)**
```python
import xml.etree.ElementTree as ET
tree = ET.parse('instrument.xpm')
root = tree.getroot()
```
- **Pros:** Built-in, no dependencies
- **Cons:** Basic functionality

**2. lxml (Recommended for complex XML)**
```python
from lxml import etree
```
- **Pros:** More powerful, XPath support, better error handling
- **Cons:** External dependency

### File Operations

**1. pathlib (Standard Library)**
```python
from pathlib import Path
```
- **Pros:** Modern, cross-platform path handling
- **Cons:** None

**2. os and shutil (Standard Library)**
```python
import os, shutil
```
- **Pros:** Comprehensive file operations
- **Cons:** Less modern API than pathlib

## Project Architecture

### Phase 1: Research & Planning (Current)
- [x] Investigate Kontakt format structure
- [x] Investigate MPCe/XPM format structure
- [x] Research similar projects
- [x] Identify Python libraries
- [ ] Create detailed PLAN.md

### Phase 2: Core Infrastructure
- [ ] Set up Python project structure
  - [ ] Create `pyproject.toml` or `setup.py`
  - [ ] Define dependencies (pydub, lxml, etc.)
  - [ ] Set up virtual environment
- [ ] Create basic CLI interface
  - [ ] Argument parsing (input/output paths)
  - [ ] Logging infrastructure
  - [ ] Error handling framework
- [ ] Implement audio file utilities
  - [ ] Format detection (WAV, AIFF, NCW)
  - [ ] Conversion utilities (AIFF→WAV, etc.)
  - [ ] Sample rate/bit depth normalization
  - [ ] File validation

### Phase 3: Kontakt Parser
- [ ] Research Kontakt 5-8 binary format
  - [ ] Analyze sample NKI files with hex editor
  - [ ] Document structure changes vs. v4
  - [ ] Identify zone/group data structures
- [ ] Implement NKI parser (Option A: Direct binary parsing)
  - [ ] File header reading
  - [ ] Zone extraction
  - [ ] Group extraction
  - [ ] Sample reference extraction
  - [ ] Metadata extraction
- [ ] Implement NKI parser (Option B: Use nkitool wrapper)
  - [ ] Python subprocess wrapper for nkitool
  - [ ] Parse nkitool XML output
  - [ ] Extract SFZ data
- [ ] Create intermediate data model
  - [ ] Zone class (key range, velocity range, sample path)
  - [ ] Group class (collection of zones)
  - [ ] Instrument class (metadata + groups)

### Phase 4: XPM Generator
- [ ] Study XPM format in detail
  - [ ] Analyze sample .xpm files
  - [ ] Document all XML tags and attributes
  - [ ] Identify required vs. optional fields
  - [ ] Test with actual MPC hardware/software
- [ ] Implement XPM writer
  - [ ] XML structure generation
  - [ ] Zone mapping
  - [ ] Sample path handling (relative paths)
  - [ ] Metadata embedding
- [ ] Create sample organization utilities
  - [ ] Copy/organize WAV files
  - [ ] Maintain folder structure
  - [ ] Handle filename conflicts
  - [ ] Generate .xpn packages (optional)

### Phase 5: Conversion Pipeline
- [ ] Integrate all components
  - [ ] NKI → Intermediate format
  - [ ] Audio conversion pipeline
  - [ ] Intermediate format → XPM
- [ ] Implement mapping logic
  - [ ] Key range translation
  - [ ] Velocity layer mapping
  - [ ] Root note handling
  - [ ] Volume/pan translation
  - [ ] Handle edge cases (overlapping zones, etc.)
- [ ] Add validation
  - [ ] Verify all samples referenced
  - [ ] Check for missing files
  - [ ] Validate XML structure
  - [ ] Test with MPC software

### Phase 6: Testing & Refinement
- [ ] Unit tests
  - [ ] Audio conversion functions
  - [ ] XML generation
  - [ ] Path handling
- [ ] Integration tests
  - [ ] End-to-end conversion
  - [ ] Various Kontakt versions
  - [ ] Different instrument types
- [ ] Real-world testing
  - [ ] Test with actual Kontakt libraries
  - [ ] Verify on MPC hardware/software
  - [ ] User acceptance testing
- [ ] Performance optimization
  - [ ] Large library handling
  - [ ] Memory efficiency
  - [ ] Parallel processing (optional)

### Phase 7: Documentation & Distribution
- [ ] User documentation
  - [ ] Installation guide
  - [ ] Usage examples
  - [ ] Troubleshooting
  - [ ] Limitations and known issues
- [ ] Developer documentation
  - [ ] API documentation
  - [ ] Architecture overview
  - [ ] Contributing guidelines
- [ ] Distribution
  - [ ] PyPI package
  - [ ] Binary releases (optional)
  - [ ] Docker image (optional)

## Technical Challenges & Solutions

### Challenge 1: Kontakt 5-8 Format Changes
**Problem:** Kontakt 5+ uses updated binary format with limited public documentation.

**Solutions:**
- **Option A:** Reverse engineer format through hex analysis of sample files
- **Option B:** Use nkitool for v4 files, manual conversion for v5+
- **Option C:** Focus on SFZ as intermediate format (use Kontakt's built-in export if available)
- **Option D:** Extract samples and metadata separately, rebuild mapping from scratch

**Recommendation:** Start with Option B (nkitool for older files) and Option D (manual mapping for newer files) while researching Option A for future improvements.

### Challenge 2: NCW Audio Format
**Problem:** NCW is proprietary and requires Kontakt to decode.

**Solutions:**
- **Option A:** Require users to pre-convert NCW to WAV using Kontakt
- **Option B:** Integrate with Kontakt's batch conversion tools
- **Option C:** Document manual conversion process

**Recommendation:** Option A (user pre-conversion) with clear documentation. This is standard practice in the community.

### Challenge 3: Advanced Kontakt Features
**Problem:** Kontakt has effects, modulation, scripting that don't exist in MPC.

**Solutions:**
- **Approach:** Clearly scope the project to sample mapping only
- **Documentation:** List unsupported features prominently
- **Future:** Consider simple parameter mapping where possible (e.g., volume, pan)

**Recommendation:** Start with basic zone mapping, gradually add supported parameters.

### Challenge 4: Testing Without Hardware
**Problem:** May not have access to physical MPC hardware for testing.

**Solutions:**
- **Option A:** Use MPC Software (available as demo/trial)
- **Option B:** Validate XML structure programmatically
- **Option C:** Compare with known-good XPM files

**Recommendation:** Combination of all three, prioritize MPC Software testing.

## Minimum Viable Product (MVP)

### MVP Scope
A command-line tool that:
1. Takes a Kontakt NKI file (v1-4) as input
2. Extracts sample mapping information
3. Converts referenced audio files to WAV
4. Generates a valid XPM file with basic zone mapping
5. Organizes output files in MPC-compatible folder structure

### MVP Deliverables
- [ ] Python CLI tool
- [ ] Basic NKI parsing (using nkitool wrapper)
- [ ] Audio format conversion (AIFF/WAV)
- [ ] XPM generation with zone mapping
- [ ] README with installation and usage instructions
- [ ] Sample test files and expected outputs

### MVP Success Criteria
- Successfully converts at least 3 different Kontakt instruments
- Generated XPM loads in MPC Software without errors
- Samples play back at correct pitches
- Key ranges map correctly
- Velocity layers preserved (if present)

## Future Enhancements

### Post-MVP Features
- GUI application
- Batch conversion mode
- Kontakt 5-8 direct support (without nkitool)
- More parameter mapping (envelopes, filters where compatible)
- Round-robin and keyswitch handling
- SFZ as alternative output format
- Reverse conversion (XPM → NKI where possible)
- Web-based converter service

### Community Engagement
- Open-source release on GitHub
- Accept contributions and feedback
- Build library of tested conversions
- Create video tutorials
- Engage with MPC and Kontakt communities

## Development Timeline (Estimated)

### Week 1-2: Foundation
- Project setup and infrastructure
- Audio conversion utilities
- Basic XML handling

### Week 3-4: Kontakt Parsing
- nkitool integration
- Data model creation
- Sample extraction

### Week 5-6: XPM Generation
- XML structure implementation
- Zone mapping logic
- File organization

### Week 7-8: Integration & Testing
- End-to-end pipeline
- Testing with real instruments
- Bug fixes and refinement

### Week 9-10: Documentation & Release
- User documentation
- Example projects
- Initial release (v0.1.0)

## Resources and References

### Official Documentation
- Kontakt Manual: https://native-instruments.com/ni-tech-manuals/
- MPC Software Manual: https://www.akaipro.com/
- SFZ Format Specification: https://sfzformat.com/

### Tools
- ConvertWithMoss: https://www.mossgrabers.de/Software/ConvertWithMoss/
- nkitool: https://github.com/reales/nkitool
- FFmpeg: https://ffmpeg.org/

### Community Resources
- VI-Control Forums: https://vi-control.net/
- KVR Audio Forums: https://www.kvraudio.com/forum/
- Gearspace: https://gearspace.com/
- MPC Forums: https://www.mpc-forums.com/

### Python Libraries
- PyDub: https://github.com/jiaaro/pydub
- lxml: https://lxml.de/
- soundfile: https://python-soundfile.readthedocs.io/
- pathlib: https://docs.python.org/3/library/pathlib.html

## License Considerations

### This Project
- **Recommendation:** MIT or Apache 2.0 (permissive open-source)
- **Rationale:** Encourages adoption and contribution

### Dependencies
- PyDub: MIT License ✓
- lxml: BSD License ✓
- soundfile: BSD License ✓
- FFmpeg: LGPL/GPL (runtime dependency, not embedded) ✓
- nkitool: Check repository license (appears to be open-source)

### Legal Notes
- Kontakt format is proprietary; reverse engineering for interoperability is generally legal
- No Native Instruments code will be used
- No DRM circumvention
- Users must own legitimate Kontakt instruments
- This is a format converter, not a piracy tool

## Conclusion

This project is feasible using existing tools and Python libraries. The key is to:

1. **Leverage existing work** (nkitool, ConvertWithMoss as references)
2. **Start simple** (MVP with basic zone mapping)
3. **Iterate gradually** (add features based on user needs)
4. **Focus on common use cases** (multi-sample instruments, not complex scripted libraries)
5. **Document limitations clearly** (not all Kontakt features will convert)

The primary value proposition is **automation and convenience** for users who want to use their Kontakt libraries on MPC hardware/software without manual recreation of mappings.

Success depends on:
- Good understanding of both formats
- Robust testing with real-world instruments
- Clear communication of capabilities and limitations
- Community feedback and contribution
