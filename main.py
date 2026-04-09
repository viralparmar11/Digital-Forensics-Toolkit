from utils.file_analysis import scan_directory
from utils.hash_tools import generate_hash
from utils.memory_analysis import get_file_full_metadata
from utils.network_analysis import analyze_pcap
from utils.timeline import create_timeline
from utils.report_generator import generate_report

def main():
    print("🔍 Starting Forensics Tool...")

    # 1. Scan directory
    file_info = scan_directory("sample_data")
    
    # 2. Generate hash for 1st file
    if file_info:
        print("\n🔒 Hash for first file:")
        hash_val = generate_hash(file_info[0]['File'])
        print(f"{file_info[0]['File']} -> {hash_val}")

    # 3. Memory processes
    print("\n🧠 Running Processes:")
    file_path = "sample_data/KICT 2021.csv"
    print("\n📁 File Metadata & Hash Info:")
    metadata = get_file_full_metadata(file_path)
    for k, v in metadata.items():
        print(f"{k}: {v}")


        # 4. Analyze PCAP
        print("\n🌐 Network Packets:")
        packets = analyze_pcap("sample_data/sample.pcap")
        for pkt in packets[:5]:
            print(pkt)

    # 5. Create timeline
    timeline = create_timeline(file_info)
    print("\n🕒 File Timeline:")
    print(timeline)

    # 6. Generate report
    generate_report(file_info)

if __name__ == "__main__":
    main()
