import os

def format_and_save_persona(username, persona_blocks):
    """Writes complete persona blocks to a .txt file."""
    output_path = os.path.join("examples", f"{username}_persona.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Persona Profile for Reddit User: u/{username}\n")
        f.write("=" * 60 + "\n\n")
        for i, block in enumerate(persona_blocks, 1):
            f.write(f"--- Persona Block {i} ---\n")
            f.write(block + "\n\n")

    print(f"Persona saved to: {output_path}")
