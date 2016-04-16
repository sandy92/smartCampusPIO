"""
Import sample data for recommendation engine
"""
import predictionio
import argparse

def import_events(client, file):
  f = open(file, 'r')
  count = 0
  for line in f:
    pass
  f.close()
  print "%s events are imported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import initial data for SmartCampus recommendation engine")
  parser.add_argument('--access_key', default='invalid_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/initial-smartcampus-data.txt")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
