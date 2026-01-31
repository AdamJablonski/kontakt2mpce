# XPM File Format Examples

This document provides detailed examples of XPM (eXtensible Program Module) files for different use cases.

## Table of Contents

- [Basic Drum Kit](#basic-drum-kit)
- [MPCe Expressive Kit with Multi-Layer Pads](#mpce-expressive-kit-with-multi-layer-pads)
- [Keygroup Instrument](#keygroup-instrument)
- [Advanced Parameters](#advanced-parameters)

## Basic Drum Kit

A simple drum kit with single samples per pad:

```xml
<?xml version="1.0" encoding="utf-8"?>
<MPCProgram Name="BasicDrumKit" ProgramType="DRUM" Version="1.0">
  <NoteAssignments>
    <!-- Kick Drum -->
    <Pad PadNoteNumber="36" PadIndex="0" PadName="Kick">
      <Samples>
        <Sample SamplePath="Samples/808_Kick.wav" Layer="1"/>
      </Samples>
      <Level Value="100"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="500" Sustain="0" Release="50"/>
      </Amp>
      <Filter Type="LP" Cutoff="127" Resonance="0"/>
      <PadColor R="255" G="0" B="0"/>
    </Pad>

    <!-- Snare Drum -->
    <Pad PadNoteNumber="38" PadIndex="2" PadName="Snare">
      <Samples>
        <Sample SamplePath="Samples/808_Snare.wav" Layer="1"/>
      </Samples>
      <Level Value="95"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="300" Sustain="0" Release="40"/>
      </Amp>
      <Filter Type="LP" Cutoff="127" Resonance="0"/>
      <PadColor R="255" G="255" B="0"/>
    </Pad>

    <!-- Closed Hi-Hat -->
    <Pad PadNoteNumber="42" PadIndex="6" PadName="HH Closed">
      <Samples>
        <Sample SamplePath="Samples/HiHat_Closed.wav" Layer="1"/>
      </Samples>
      <Level Value="85"/>
      <Pan Value="20"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="100" Sustain="0" Release="20"/>
      </Amp>
      <Filter Type="HP" Cutoff="40" Resonance="10"/>
      <MuteGroup Group="1"/>
      <PadColor R="100" G="100" B="255"/>
    </Pad>

    <!-- Open Hi-Hat -->
    <Pad PadNoteNumber="46" PadIndex="10" PadName="HH Open">
      <Samples>
        <Sample SamplePath="Samples/HiHat_Open.wav" Layer="1"/>
      </Samples>
      <Level Value="85"/>
      <Pan Value="20"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="800" Sustain="0" Release="100"/>
      </Amp>
      <Filter Type="HP" Cutoff="40" Resonance="10"/>
      <MuteGroup Group="1"/>
      <PadColor R="150" G="150" B="255"/>
    </Pad>

    <!-- Clap -->
    <Pad PadNoteNumber="39" PadIndex="3" PadName="Clap">
      <Samples>
        <Sample SamplePath="Samples/Clap.wav" Layer="1"/>
      </Samples>
      <Level Value="90"/>
      <Pan Value="-10"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="250" Sustain="0" Release="30"/>
      </Amp>
      <Filter Type="LP" Cutoff="100" Resonance="5"/>
      <PadColor R="255" G="128" B="0"/>
    </Pad>

    <!-- Tom 1 -->
    <Pad PadNoteNumber="48" PadIndex="12" PadName="Tom 1">
      <Samples>
        <Sample SamplePath="Samples/Tom_High.wav" Layer="1"/>
      </Samples>
      <Level Value="92"/>
      <Pan Value="-15"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="400" Sustain="0" Release="50"/>
      </Amp>
      <Filter Type="LP" Cutoff="110" Resonance="0"/>
      <PadColor R="0" G="255" B="0"/>
    </Pad>

    <!-- Tom 2 -->
    <Pad PadNoteNumber="45" PadIndex="9" PadName="Tom 2">
      <Samples>
        <Sample SamplePath="Samples/Tom_Mid.wav" Layer="1"/>
      </Samples>
      <Level Value="92"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="450" Sustain="0" Release="60"/>
      </Amp>
      <Filter Type="LP" Cutoff="105" Resonance="0"/>
      <PadColor R="0" G="200" B="0"/>
    </Pad>

    <!-- Tom 3 -->
    <Pad PadNoteNumber="43" PadIndex="7" PadName="Tom 3">
      <Samples>
        <Sample SamplePath="Samples/Tom_Low.wav" Layer="1"/>
      </Samples>
      <Level Value="92"/>
      <Pan Value="15"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="500" Sustain="0" Release="70"/>
      </Amp>
      <Filter Type="LP" Cutoff="100" Resonance="0"/>
      <PadColor R="0" G="150" B="0"/>
    </Pad>
  </NoteAssignments>
  
  <GlobalSettings>
    <Master Level="100"/>
    <Polyphony Voices="32"/>
  </GlobalSettings>
</MPCProgram>
```

## MPCe Expressive Kit with Multi-Layer Pads

An example showing how to create a pad with 4 layers for corner-based expressive control:

```xml
<?xml version="1.0" encoding="utf-8"?>
<MPCProgram Name="MPCe_ExpressiveKit" ProgramType="DRUM" Version="1.0" MPCeEnabled="true">
  <NoteAssignments>
    <!-- Expressive Kick with 4 Layers -->
    <Pad PadNoteNumber="36" PadIndex="0" PadName="Kick Expressive">
      <Samples>
        <!-- Layer 1: Top-Left - Soft, Dark -->
        <Sample SamplePath="Samples/Kick_Soft_Dark.wav" Layer="1" 
                Corner="TopLeft" VelocityMin="1" VelocityMax="127"/>
        
        <!-- Layer 2: Top-Right - Soft, Bright -->
        <Sample SamplePath="Samples/Kick_Soft_Bright.wav" Layer="2" 
                Corner="TopRight" VelocityMin="1" VelocityMax="127"/>
        
        <!-- Layer 3: Bottom-Left - Hard, Dark -->
        <Sample SamplePath="Samples/Kick_Hard_Dark.wav" Layer="3" 
                Corner="BottomLeft" VelocityMin="1" VelocityMax="127"/>
        
        <!-- Layer 4: Bottom-Right - Hard, Bright -->
        <Sample SamplePath="Samples/Kick_Hard_Bright.wav" Layer="4" 
                Corner="BottomRight" VelocityMin="1" VelocityMax="127"/>
      </Samples>
      
      <ExpressiveControl Enabled="true">
        <XYMapping>
          <XAxis Parameter="LayerMix" Min="0" Max="127"/>
          <YAxis Parameter="LayerMix" Min="0" Max="127"/>
        </XYMapping>
        <BlendMode Type="Crossfade" Curve="Linear"/>
        <Modulation>
          <XModulation Target="Filter.Cutoff" Amount="50"/>
          <YModulation Target="Pitch" Amount="25"/>
        </Modulation>
      </ExpressiveControl>
      
      <Level Value="100"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="500" Sustain="0" Release="50"/>
      </Amp>
      <Filter Type="LP" Cutoff="120" Resonance="5"/>
      <PadColor R="255" G="0" B="100"/>
    </Pad>

    <!-- Expressive Snare with Velocity Layers -->
    <Pad PadNoteNumber="38" PadIndex="2" PadName="Snare Expressive">
      <Samples>
        <!-- Layer 1: Soft Hit (Low Velocity) -->
        <Sample SamplePath="Samples/Snare_Soft.wav" Layer="1" 
                VelocityMin="1" VelocityMax="40"/>
        
        <!-- Layer 2: Medium Hit -->
        <Sample SamplePath="Samples/Snare_Medium.wav" Layer="2" 
                VelocityMin="41" VelocityMax="85"/>
        
        <!-- Layer 3: Hard Hit (High Velocity) -->
        <Sample SamplePath="Samples/Snare_Hard.wav" Layer="3" 
                VelocityMin="86" VelocityMax="127"/>
        
        <!-- Layer 4: Rimshot (X position trigger) -->
        <Sample SamplePath="Samples/Snare_Rim.wav" Layer="4" 
                Corner="TopRight" VelocityMin="1" VelocityMax="127"/>
      </Samples>
      
      <ExpressiveControl Enabled="true">
        <XYMapping>
          <XAxis Parameter="SampleSelect" Min="0" Max="127"/>
          <YAxis Parameter="Velocity" Min="0" Max="127"/>
        </XYMapping>
        <BlendMode Type="VelocitySwitch"/>
      </ExpressiveControl>
      
      <Level Value="95"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="300" Sustain="0" Release="40"/>
      </Amp>
      <Filter Type="LP" Cutoff="127" Resonance="0"/>
      <PadColor R="255" G="255" B="0"/>
    </Pad>

    <!-- Expressive Hi-Hat with Articulation Control -->
    <Pad PadNoteNumber="42" PadIndex="6" PadName="HiHat Expressive">
      <Samples>
        <!-- Layer 1: Closed (Bottom-Left) -->
        <Sample SamplePath="Samples/HH_Closed.wav" Layer="1" 
                Corner="BottomLeft"/>
        
        <!-- Layer 2: Semi-Open (Top-Left) -->
        <Sample SamplePath="Samples/HH_SemiOpen.wav" Layer="2" 
                Corner="TopLeft"/>
        
        <!-- Layer 3: Open (Top-Right) -->
        <Sample SamplePath="Samples/HH_Open.wav" Layer="3" 
                Corner="TopRight"/>
        
        <!-- Layer 4: Edge Hit (Bottom-Right) -->
        <Sample SamplePath="Samples/HH_Edge.wav" Layer="4" 
                Corner="BottomRight"/>
      </Samples>
      
      <ExpressiveControl Enabled="true">
        <XYMapping>
          <XAxis Parameter="ArticulationBlend" Min="0" Max="127"/>
          <YAxis Parameter="OpenAmount" Min="0" Max="127"/>
        </XYMapping>
        <BlendMode Type="Crossfade" Curve="Exponential"/>
        <Modulation>
          <YModulation Target="Filter.Cutoff" Amount="80"/>
          <YModulation Target="Envelope.Decay" Amount="60"/>
        </Modulation>
      </ExpressiveControl>
      
      <Level Value="85"/>
      <Pan Value="20"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="0" Decay="150" Sustain="0" Release="25"/>
      </Amp>
      <Filter Type="HP" Cutoff="40" Resonance="10"/>
      <MuteGroup Group="1"/>
      <PadColor R="100" G="100" B="255"/>
    </Pad>
  </NoteAssignments>
  
  <GlobalSettings>
    <Master Level="100"/>
    <Polyphony Voices="64"/>
    <MPCeSettings>
      <ExpressiveMode Enabled="true"/>
      <XYSensitivity Value="100"/>
      <PadPressureCurve Type="Logarithmic"/>
    </MPCeSettings>
  </GlobalSettings>
</MPCProgram>
```

## Keygroup Instrument

A chromatic instrument with samples mapped across the keyboard:

```xml
<?xml version="1.0" encoding="utf-8"?>
<MPCProgram Name="BassSynth" ProgramType="KEYGROUP" Version="1.0">
  <KeyGroupAssignments>
    <!-- Low Bass Notes (C0-B0) -->
    <KeyGroup RootNote="36" LowNote="24" HighNote="35" Name="Bass Low">
      <Samples>
        <Sample SamplePath="Samples/Bass_C1.wav" Layer="1" RootKey="36"/>
      </Samples>
      <Level Value="100"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="10" Decay="300" Sustain="70" Release="100"/>
      </Amp>
      <Filter Type="LP" Cutoff="80" Resonance="20">
        <Envelope Attack="20" Decay="400" Sustain="50" Release="150" Amount="60"/>
      </Filter>
      <LFO Rate="2.5" Amount="10" Target="Filter.Cutoff" Waveform="Sine"/>
    </KeyGroup>

    <!-- Mid Bass Notes (C1-B1) -->
    <KeyGroup RootNote="48" LowNote="36" HighNote="47" Name="Bass Mid">
      <Samples>
        <Sample SamplePath="Samples/Bass_C2.wav" Layer="1" RootKey="48"/>
      </Samples>
      <Level Value="100"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="10" Decay="300" Sustain="70" Release="100"/>
      </Amp>
      <Filter Type="LP" Cutoff="80" Resonance="20">
        <Envelope Attack="20" Decay="400" Sustain="50" Release="150" Amount="60"/>
      </Filter>
      <LFO Rate="2.5" Amount="10" Target="Filter.Cutoff" Waveform="Sine"/>
    </KeyGroup>

    <!-- High Bass Notes (C2-B2) -->
    <KeyGroup RootNote="60" LowNote="48" HighNote="71" Name="Bass High">
      <Samples>
        <Sample SamplePath="Samples/Bass_C3.wav" Layer="1" RootKey="60"/>
      </Samples>
      <Level Value="100"/>
      <Pan Value="0"/>
      <Tuning Coarse="0" Fine="0"/>
      <Amp>
        <Envelope Attack="10" Decay="300" Sustain="70" Release="100"/>
      </Amp>
      <Filter Type="LP" Cutoff="80" Resonance="20">
        <Envelope Attack="20" Decay="400" Sustain="50" Release="150" Amount="60"/>
      </Filter>
      <LFO Rate="2.5" Amount="10" Target="Filter.Cutoff" Waveform="Sine"/>
    </KeyGroup>
  </KeyGroupAssignments>
  
  <GlobalSettings>
    <Master Level="100"/>
    <Polyphony Voices="16" VoiceMode="Poly"/>
    <Portamento Time="0" Mode="Off"/>
    <PitchBend Range="2"/>
    <Modulation>
      <ModWheel Target="Filter.Cutoff" Amount="50"/>
      <Aftertouch Target="LFO.Amount" Amount="30"/>
    </Modulation>
  </GlobalSettings>
</MPCProgram>
```

## Advanced Parameters

### Comprehensive Pad Configuration

```xml
<Pad PadNoteNumber="36" PadIndex="0" PadName="Advanced Kick">
  <Samples>
    <Sample SamplePath="Samples/Kick.wav" Layer="1" 
            SampleStart="0" SampleEnd="44100" LoopMode="Off"
            RootKey="36" FineTune="0" PlayMode="OneShot"/>
  </Samples>
  
  <!-- Volume and Pan -->
  <Level Value="100" VelocityDepth="80"/>
  <Pan Value="0" Random="5"/>
  
  <!-- Tuning -->
  <Tuning Coarse="0" Fine="0" VelocityDepth="10"/>
  
  <!-- Amplitude Envelope -->
  <Amp>
    <Envelope Attack="0" Decay="500" Sustain="0" Release="50" 
              VelocityDepth="50" Curve="Exponential"/>
  </Amp>
  
  <!-- Filter -->
  <Filter Type="LP" Cutoff="120" Resonance="5" VelocityDepth="30">
    <Envelope Attack="5" Decay="400" Sustain="20" Release="100" 
              Amount="70" Curve="Linear"/>
  </Filter>
  
  <!-- LFO -->
  <LFO Rate="4.0" Amount="20" Target="Pitch" Waveform="Sine" 
       Phase="0" Sync="Off" Retrigger="On"/>
  
  <!-- Effects Sends -->
  <Effects>
    <Send Destination="Reverb" Level="20"/>
    <Send Destination="Delay" Level="0"/>
    <Send Destination="Chorus" Level="0"/>
  </Effects>
  
  <!-- Mute/Solo Groups -->
  <MuteGroup Group="0"/>
  <SoloGroup Group="0"/>
  
  <!-- MIDI -->
  <MIDI OutputNote="36" Channel="10" VelocityCurve="Linear"/>
  
  <!-- Visual -->
  <PadColor R="255" G="0" B="0"/>
  
  <!-- Playback -->
  <Playback Mode="OneShot" Priority="High" Polyphony="4"/>
  
  <!-- Time Stretch -->
  <TimeStretch Enabled="false" Mode="Standard" Ratio="1.0"/>
</Pad>
```

### Effect Parameters

```xml
<GlobalSettings>
  <Effects>
    <!-- Reverb -->
    <Reverb Enabled="true">
      <Type Value="Hall"/>
      <Time Value="2.5"/>
      <PreDelay Value="20"/>
      <Diffusion Value="70"/>
      <Damping Value="50"/>
      <Mix Value="30"/>
    </Reverb>
    
    <!-- Delay -->
    <Delay Enabled="true">
      <Type Value="Stereo"/>
      <Time Left="500" Right="750" Sync="Off"/>
      <Feedback Value="40"/>
      <Filter Type="HP" Cutoff="200"/>
      <Mix Value="25"/>
    </Delay>
    
    <!-- Chorus -->
    <Chorus Enabled="false">
      <Rate Value="1.5"/>
      <Depth Value="50"/>
      <Mix Value="20"/>
    </Chorus>
    
    <!-- Master EQ -->
    <EQ>
      <Band Type="LowShelf" Frequency="80" Gain="0" Q="0.7"/>
      <Band Type="Peak" Frequency="500" Gain="0" Q="1.0"/>
      <Band Type="Peak" Frequency="2000" Gain="0" Q="1.0"/>
      <Band Type="HighShelf" Frequency="8000" Gain="0" Q="0.7"/>
    </EQ>
    
    <!-- Master Compressor -->
    <Compressor Enabled="false">
      <Threshold Value="-10"/>
      <Ratio Value="4"/>
      <Attack Value="5"/>
      <Release Value="100"/>
      <MakeupGain Value="3"/>
    </Compressor>
  </Effects>
</GlobalSettings>
```

## Notes on XPM Examples

### Important Considerations

1. **XML Structure**: The examples above are conceptual and based on observed behavior. The actual XPM format may have different element names and structures.

2. **MPCe Elements**: Elements like `<ExpressiveControl>`, `Corner`, and X/Y mapping parameters are inferred from MPCe functionality. The actual implementation may differ.

3. **Validation**: XPM files should be created using MPC software for guaranteed compatibility. Hand-editing is possible but requires careful attention to format.

4. **Relative Paths**: Always use relative paths for samples to ensure portability.

5. **Testing**: Test all XPM files on actual hardware or MPC software before distribution.

### Creating Valid XPM Files

For production use:

1. Use MPC Software to create and save programs
2. Use Expansion Builder for packaging
3. Examine generated XPM files to understand structure
4. Make careful edits if needed
5. Always validate on target hardware

## Additional Resources

- See `mpce-format.md` for complete format documentation
- See `expansion-creation.md` for packaging workflows
- Official Akai documentation for latest specifications
