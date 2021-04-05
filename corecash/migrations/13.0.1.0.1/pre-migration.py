def migrate(cr, version):
    if not version:
        return
    # Removing old translations
    cr.execute("""UPDATE account_move_line
    SET currency_id=2
    WHERE id IN (4624, 37408, 27178, 26883, 27039);
    """)
