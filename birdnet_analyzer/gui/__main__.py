if __name__ == "__main__":
    import birdnet_analyzer.gui.utils as gu
    import birdnet_analyzer.gui.single_file as sfa
    import birdnet_analyzer.gui.multi_file as mfa
    import birdnet_analyzer.gui.train as train
    import birdnet_analyzer.gui.segments as gs
    import birdnet_analyzer.gui.review as review
    import birdnet_analyzer.gui.species as species

    gu.open_window(
        [
            sfa.build_single_analysis_tab,
            mfa.build_multi_analysis_tab,
            train.build_train_tab,
            gs.build_segments_tab,
            review.build_review_tab,
            species.build_species_tab,
        ]
    )