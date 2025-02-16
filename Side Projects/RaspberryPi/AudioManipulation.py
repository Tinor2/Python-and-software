import librosa
import csv
def read_audio_to_list_librosa(audio_file_path):
  """Reads an audio file using librosa and returns a list of amplitude values.

  Args:
    audio_file_path: The path to the audio file.

  Returns:
    A list of amplitude values.
  """

  y, sr = librosa.load(audio_file_path, sr = 800)
  amplitude_values = y.tolist()

  return amplitude_values

# Example usage:
audio_file = "audio.wav"
amplitude_data = read_audio_to_list_librosa("/Users/ronitbhandari/Downloads/family-ties.wav")

i = 0
data_as_list_of_lists = [[value] for value in amplitude_data]
with open("data.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(data_as_list_of_lists)
  i += 1
