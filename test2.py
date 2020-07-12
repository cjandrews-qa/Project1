import asyncio
import chess
import chess.engine

async def main():
    transport, engine = await chess.engine.popen_uci("/usr/bin/stockfish")

    board = chess.Board()
    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=0.1))
        board.push(result.move)

    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())