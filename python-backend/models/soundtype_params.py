# -*- encoding: utf-8 -*-

class SoundtypeParams(object):
    def __init__(self, file_name, leq_mean, leq_std, leq_25, leq_median, leq_75, leq_10_90, loudness_mean, loudness_std,
                 loudness_25, loudness_median, loudness_75, loudness_10_90, roughness_mean, roughness_std, roughness_25,
                 roughness_median, roughness_75, roughness_10_90, sharpness_mean, sharpness_std, sharpness_25,
                 sharpness_median, sharpness_75, sharpness_10_90, fluct_mean, fluct_std, fluct_25, fluct_median,
                 fluct_75, fluct_10_90, tonality_mean, tonality_std, tonality_25, tonality_median, tonality_75,
                 tonality_10_90) -> None:
        self.file_name = file_name
        self.leq_mean = leq_mean
        self.leq_std = leq_std
        self.leq_25 = leq_25
        self.leq_median = leq_median
        self.leq_75 = leq_75
        self.leq_10_90 = leq_10_90
        self.loudness_mean = loudness_mean
        self.loudness_std = loudness_std
        self.loudness_25 = loudness_25
        self.loudness_median = loudness_median
        self.loudness_75 = loudness_75
        self.loudness_10_90 = loudness_10_90
        self.roughness_mean = roughness_mean
        self.roughness_std = roughness_std
        self.roughness_25 = roughness_25
        self.roughness_median = roughness_median
        self.roughness_75 = roughness_75
        self.roughness_10_90 = roughness_10_90
        self.sharpness_mean = sharpness_mean
        self.sharpness_std = sharpness_std
        self.sharpness_25 = sharpness_25
        self.sharpness_median = sharpness_median
        self.sharpness_75 = sharpness_75
        self.sharpness_10_90 = sharpness_10_90
        self.fluct_mean = fluct_mean
        self.fluct_std = fluct_std
        self.fluct_25 = fluct_25
        self.fluct_median = fluct_median
        self.fluct_75 = fluct_75
        self.fluct_10_90 = fluct_10_90
        self.tonality_mean = tonality_mean
        self.tonality_std = tonality_std
        self.tonality_25 = tonality_25
        self.tonality_median = tonality_median
        self.tonality_75 = tonality_75
        self.tonality_10_90 = tonality_10_90
