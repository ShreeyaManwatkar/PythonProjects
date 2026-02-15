def hanoi_solver(n):
    # Initialize the three rods
    source = list(range(n, 0, -1))   # [n, n-1, ..., 1]
    auxiliary = []
    destination = []

    result = []

    result.append(f"{source} {auxiliary} {destination}")

    def move_disks(num, src, aux, dest):
        if num == 1:
            disk = src.pop()
            dest.append(disk)
            result.append(f"{source} {auxiliary} {destination}")
            return

        # Step 1: Move n-1 disks from source to auxiliary
        move_disks(num - 1, src, dest, aux)

        # Step 2: Move the largest disk to destination
        disk = src.pop()
        dest.append(disk)
        result.append(f"{source} {auxiliary} {destination}")

        # Step 3: Move n-1 disks from auxiliary to destination
        move_disks(num - 1, aux, src, dest)

    move_disks(n, source, auxiliary, destination)
    
    return "\n".join(result)
