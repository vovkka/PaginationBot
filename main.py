import asyncio
import logging
from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config

# Logger initialization
logger = logging.getLogger(__name__)


async def main() -> None:
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config()
    bot = Bot(config.token, parse_mode='HTML')
    dp = Dispatcher()

    #dp.include_routers()

    # Skip updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

