def fcfs(requests, initial_head):
  """
  FCFS algorithm for disk scheduling
  """
  total_movement = 0
  for request in requests:
    movement = abs(request - initial_head)
    total_movement += movement
    initial_head = request
  return total_movement

def scan(requests, initial_head):
  """
  SCAN algorithm for disk scheduling
  """
  requests.sort()
  total_movement = abs(requests[0] - initial_head)
  for i in range(1, len(requests)):
    movement = abs(requests[i] - requests[i-1])
    total_movement += movement
  # Move to the other end and serve remaining requests
  total_movement += abs(requests[-1] - 4999)
  for i in range(len(requests) - 2, -1, -1):
    movement = abs(requests[i] - requests[i+1])
    total_movement += movement
  return total_movement

def cscan(requests, initial_head):
  """
  C-SCAN algorithm for disk scheduling
  """
  requests.sort()
  total_movement = abs(requests[0] - initial_head)
  for i in range(1, len(requests)):
    movement = abs(requests[i] - requests[i-1])
    total_movement += movement
  # Move to the other end and come back to 0
  total_movement += abs(requests[-1] - 0)
  for i in range(len(requests) - 1, 0, -1):
    movement = abs(requests[i] - requests[i-1])
    total_movement += movement
  return total_movement

def main():
  import sys

  if len(sys.argv) != 3:
    print("Usage: python", sys.argv[0], "<initial_head> <request_file>")
    exit(1)

  initial_head = int(sys.argv[1])
  request_file = sys.argv[2]

  requests = []
  with open(request_file, 'r') as f:
    for line in f:
      requests.append(int(line.strip()))

  # Task 1 - Service requests as they appear
  print("FCFS Total Head Movement:", fcfs(requests.copy(), initial_head))
  print("SCAN Total Head Movement:", scan(requests.copy(), initial_head))
  print("C-SCAN Total Head Movement:", cscan(requests.copy(), initial_head))

  # Task 2 - Rearrange requests for minimum movement
  print("\nFCFS Rearranged Total Head Movement:", fcfs(requests, initial_head))
  print("SCAN Rearranged Total Head Movement (Already Sorted):", scan(requests, initial_head))
  print("C-SCAN Rearranged Total Head Movement (Already Sorted):", cscan(requests, initial_head))

if __name__ == "__main__":
  main()
