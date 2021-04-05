1   def migrate(cr, version):
  1     if not version:
  2         return
  3     # Removing old translations
  4     cr.execute("""
  5         UPDATE account_move_line SET
            currency_id=2
            WHERE id IN (4624, 37408, 27178, 26883, 27039);
 11     """)
