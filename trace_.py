def read_trace(trace_file):
    trace_data = []
    try:
        with open(trace_file, 'r') as trace:
            lines = trace.readlines()
            for line in lines:
                line = line.strip()
                trace_data.append(line)

        return trace_data
    
    except Exception as e:
        print(f'Error while reading trace file: {e}')
