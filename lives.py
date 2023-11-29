# visual stages of the game, the index of each stage corresponds to number of tries the user has left. used to dispay current stage of game.
def display_hangman(tries):
   stages = [
      """
      No more lives remaining!
      """,

      """
      ☠️ (1 life remaining)
      """,

      """
      ☠️☠️ (2 lives remaining)
      """,

      """
      ☠️☠️☠️ (3 lives remaining)
      """,

      """
      ☠️☠️☠️☠️ (4 lives remaining)
      """,

      """
      ☠️☠️☠️☠️☠️ (5 lives remaining)
      """,

      """
      ☠️☠️☠️☠️☠️☠️ (6 lives remaining)
      """
    ]
   return stages[tries]
