import asyncio
import os
import django

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from rewards import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gw_rewards/gw_rewards/settings.py")
django.setup()


async def main():

    transport = AIOHTTPTransport(
        url="https://api.sorare.com/graphql",
        # headers = {"Authorization": "Bearer <TheUserAccessToken>"}
    )

    async with Client(transport=transport) as session:

        query = gql(
            """
            query {
  so5 {
    so5Fixture {
      gameWeek
      displayName
      so5Leagues {
        so5Leaderboards {
          displayName
          rewardedLineupsCount
          rarityType
          so5LineupsCount
        }
      }
    }
  }
}

        """
        )

        result = await session.execute(query)

        for card in result["so5"]["so5Fixture"]["so5Leagues"]:
            print(f" ГВ: {result['so5']['so5Fixture']['gameWeek']} Лига: {card['so5Leaderboards']}")
            # league = Leagues(name=card['so5Leaderboards']['displayName'], rarity=card['so5Leaderboards']['rarityType'])
            for obj in card['so5Leaderboards']:
                print(obj['displayName'], obj['rarityType'])
                league = models.Leagues(name=obj['displayName'],
                                 rarity=obj['rarityType'])
                league.save()
            # print(card['so5Leaderboards']['displayName'], ))
            # reward = Rewards(gw = result['so5']['so5Fixture']['gameWeek'], prizepool = )
        # for card in result["so5"]["so5Fixture"]["gameWeek"]:
        # print(result["so5"]["so5Fixture"]["gameWeek"])
        # print(result["so5"]["so5Fixture"]["gameWeek"])


asyncio.run(main())