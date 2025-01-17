from aiohttp import web
import csv


async def get_movie(request):
    with open('movies.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            print(row)
    return web.json_response({'hello': 'world'})


app = web.Application()
app.add_routes([web.get('/', get_movie)])


if __name__ == '__main__':
    web.run_app(app)