from asyncio import new_event_loop, set_event_loop

from app import Application


if __name__ == "__main__":
    app = Application()

    loop = new_event_loop()
    set_event_loop(loop)

    loop.run_until_complete(app.start())
