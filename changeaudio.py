from pydub import AudioSegment

def slow_down_audio(input_file, output_file, target_duration):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    
    # Get the original duration of the audio in milliseconds
    original_duration = len(audio)
    
    # Calculate the playback speed factor
    target_duration_ms = target_duration * 1000  # Convert seconds to milliseconds
    speed_factor = original_duration / target_duration_ms
    
    if speed_factor > 0:
        # Apply speed adjustment
        slowed_audio = audio._spawn(audio.raw_data, overrides={
            "frame_rate": int(audio.frame_rate * speed_factor)
        }).set_frame_rate(audio.frame_rate)
        
        # Export the slowed audio
        slowed_audio.export(output_file, format="mp3")
        print(f"Audio slowed down and saved to {output_file}")
    else:
        print("Target duration must be greater than the original duration.")

# Example usage
slow_down_audio("countdown (2).mp3", "output_audio.mp3", 10)


