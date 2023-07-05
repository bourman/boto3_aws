import boto3
from time import sleep
def get_next_available_number(ec2_console, machine_name_prefix):
    response = ec2_console.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [f'{machine_name_prefix}*']
            },
        ]
    )
    instances = response['Reservations']
    count = len(instances)
    return count + 1
while True:
    choice = input("\nAutomatically create virtual machines:\n1. Create Windows VMs\n2. Create Linux VMs\n")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            while True:
                windows_count = input("Enter the number of Windows machines: ")
                if windows_count.isdigit():
                    windows_count = int(windows_count)
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
            # AWS EC2 instance creation for Windows
            aws_management_console = boto3.session.Session(profile_name="default")
            ec2_console = aws_management_console.client('ec2')
            for i in range(1, windows_count + 1):
                machine_number = get_next_available_number(ec2_console, 'window')
                response = ec2_console.run_instances(
                    ImageId='ami-0d2f97c8735a48a15',
                    InstanceType='t2.micro',
                    MaxCount=1,
                    MinCount=1,
                    TagSpecifications=[
                        {
                            'ResourceType': 'instance',
                            'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': f'window{machine_number}'
                                },
                            ]
                        },
                    ]
                )
            print("\n----\nDone, go check on AWS EC2\n----\n")
        elif choice == 2:
            while True:
                linux_count = input("Enter the number of Linux machines: ")
                if linux_count.isdigit():
                    linux_count = int(linux_count)
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
            # AWS EC2 instance creation for Linux
            aws_management_console = boto3.session.Session(profile_name="default")
            ec2_console = aws_management_console.client('ec2')
            for i in range(1, linux_count + 1):
                machine_number = get_next_available_number(ec2_console, 'linux')
                response = ec2_console.run_instances(
                    ImageId='ami-03f38e546e3dc59e1',
                    InstanceType='t2.micro',
                    MaxCount=1,
                    MinCount=1,
                    TagSpecifications=[
                        {
                            'ResourceType': 'instance',
                            'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': f'linux{machine_number}'
                                },
                            ]
                        },
                    ]
                )
            print("\n----\nDone, go check on AWS EC2\n----\n")
        else:
            print("Invalid choice. Please enter a valid option.")
    else:
        print("Invalid input. Please enter a valid number for the choice.")
    while True:
        exit_choice = input("Do you want to exit? (yes/no): ")
        if exit_choice.lower() == "yes":
            break
        elif exit_choice.lower() == "no":
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
    if exit_choice.lower() == "yes":
        break
print("Goodbye!")
