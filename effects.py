# goh_effect/effects.py

class Effect:
    def apply(self, audio_data):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах.")

class Echo(Effect):
    def apply(self, audio_data, delay=0.2, decay=0.5):
        # Эффект эха
        delay_samples = int(delay * 44100)  # Примерная частота дискретизации
        output = audio_data[:] + [0] * delay_samples
        for i in range(len(audio_data)):
            if i + delay_samples < len(output):
                output[i + delay_samples] += audio_data[i] * decay
        return output

class Reverb(Effect):
    def apply(self, audio_data):
        # Эффект реверберации
        reverb_data = []
        for i in range(len(audio_data)):
            reverb_sample = audio_data[i] * 0.5  # Примерная реверберация
            if i > 10:
                reverb_sample += audio_data[i - 10] * 0.5
            reverb_data.append(reverb_sample)
        return reverb_data

class Distortion(Effect):
    def apply(self, audio_data, gain=5):
        # Эффект искажения
        return [min(max(sample * gain, -1), 1) for sample in audio_data]

class Chorus(Effect):
    def apply(self, audio_data, depth=0.5, rate=1.5):
        # Эффект хора
        output = []
        for i in range(len(audio_data)):
            modulated_sample = int(depth * (i % int(rate * 44100)))
            if i - modulated_sample >= 0:
                output.append(audio_data[i] + audio_data[i - modulated_sample] * 0.5)
            else:
                output.append(audio_data[i])
        return output

class Flanger(Effect):
    def apply(self, audio_data, depth=0.5, rate=1.0):
        # Эффект фленжера
        output = []
        for i in range(len(audio_data)):
            modulated_sample = int(depth * (i % int(rate * 44100)))
            if i - modulated_sample >= 0:
                output.append(audio_data[i] + audio_data[i - modulated_sample] * 0.5)
            else:
                output.append(audio_data[i])
        return output