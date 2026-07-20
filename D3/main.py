"""
Day 3: Testing Multiple Methods & Object State
Classes: TokenCounter, ConservationMemory, EpochCounter, DatasetTracker, ModelVersion
"""

from p1_token_counter import TokenCounter
from p2_conversation_memory import ConservationMemory
from p3_epoch_counter import EpochCounter
from p4_dataset_tracker import DatasetTracker
from p5_model_version import ModelVersion


def main():
    print("=" * 40)
    print("DAY 3 — TESTING ALL CLASSES")
    print("=" * 40)

    # 1. TokenCounter
    print("\n1. TokenCounter")
    tc = TokenCounter("Explain Artificial Intelligence and Machine Learning")
    tc.show_prompt()
    tc.count_tokens()

    # 2. ConservationMemory (ConversationMemory)
    print("\n2. ConservationMemory")
    msg = ConservationMemory()
    msg.show_count()
    msg.add_message()
    msg.add_message()
    msg.show_count()

    # 3. EpochCounter
    print("\n3. EpochCounter")
    epoch = EpochCounter()
    epoch.show_epoch()
    epoch.increase_epoch()
    epoch.increase_epoch()
    epoch.increase_epoch()
    epoch.show_epoch()

    # 4. DatasetTracker
    print("\n4. DatasetTracker")
    ds = DatasetTracker("Titanic Dataset")
    ds.show_dataset()
    ds.update_dataset("Iris Dataset")
    ds.show_dataset()

    # 5. ModelVersion
    print("\n5. ModelVersion")
    mv = ModelVersion("v1.0")
    mv.show_version()
    mv.update_version("v2.0")
    mv.show_version()

    print("\n" + "=" * 40)
    print("DAY 3 COMPLETE!")
    print("=" * 40)


if __name__ == "__main__":
    main()