command_parts = command.split()

if not command_parts:
    continue

cmd = command_parts[0]
args = command_parts[1:]

if cmd == "add":
    add_contact(args)
elif cmd == "change":
    change_contact(args)
elif cmd == "phone":
    show_phone(args)
elif cmd == "all":
    show_all()
elif cmd in ["exit", "close"]:
    break
else:
    print("Невідома команда")
