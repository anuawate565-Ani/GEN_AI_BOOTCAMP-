"""
Day 2: Testing all 5 classes.
Entry point for Day 2 bootcamp.
"""

from p1_learning_rate_manager import LearningRateManager
from p2_chatbot import ChatBot
from p3_translate import Translate
from p4_car import Car
from p5_rectangle import Rectangle


def main():
    print("=" * 40)
    print("DAY 2 — TESTING ALL CLASSES")
    print("=" * 40)

    # 1. Learning Rate Manager
    print("\n1. LearningRateManager")
    lr = LearningRateManager(0.001)
    print(f"Learning Rate: {lr.get_learning_rate()}")

    # 2. ChatBot
    print("\n2. ChatBot")
    bot = ChatBot()
    bot.ask("What is AI?")
    bot.ask("Explain Python")

    # 3. Translate
    print("\n3. Translate")
    sentence = Translate()
    sentence.translation("Hello")
    sentence.translation("Machine Learning")

    # 4. Car
    print("\n4. Car")
    cars = Car()
    cars.brand("BMW M5", "Rolls Royce Phantom")

    # 5. Rectangle
    print("\n5. Rectangle")
    rect = Rectangle()
    result = rect.area(5, 4)
    print(f"Area: {result}")

    print("\n" + "=" * 40)
    print("DAY 2 COMPLETE!")
    print("=" * 40)


if __name__ == "__main__":
    main()