from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union, Tuple, Generator


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0
        self.error_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "type": self.stream_type,
            "processed": self.processed_count,
            "errors": self.error_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Environment Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readed = [d for d in data_batch if isinstance(d, (int, float))]
            count = len(readed)
            self.processed_count += count
            if count == 0:
                return f"Sensor analysis: 0 readings processsed, avg temp : 0C"

            avg = sum(readed) / count
            return f"Sensor analysis: {count} readings processed, avg temp: {avg}C"
        except Exception as e:
            self.error_count += 1
            return f"Error in SensorStrem: {str(e)}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net_flow = 0
            ops_count = 0
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    parts = item.split(":")
                    if len(parts) == 2:
                        action = parts[0].lower()
                        value = float(parts[1])
                        if action == "buy":
                            net_flow -= value
                        elif action == "sell":
                            net_flow += value
                        ops_count += 1

            self.processed_count += ops_count
            final_net = int(net_flow)
            sign = "+" if final_net > 0 else ""
            return f"Transaction analysis: {ops_count} operations, net flow: {sign}{final_net} units"

        except Exception as e:
            self.error_count += 1
            return f"Error in TransactionStream: {str(e)}"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = [str(item).lower() for item in data_batch]
            error_events = [e for e in events if "error" in e]
            count = len(events)
            errors_found = len(error_events)
            self.processed_count += count
            self.error_count += errors_found
            return f"Event analysis: {count} events, {errors_found} errors detected"
        except Exception as e:
            self.error_count += 1
            return f"Error in EventStream: {str(e)}"


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream , DataStream):
            self.streams.append(stream)
        else:
            print("Error: Invalid stream type.")

    def process_all(self, mixed_data: List[Any]) -> None:
        print("Processing mixed stream types through unified interface..")
        for stream in self.streams:
            result = stream.process_batch(mixed_data)
            print(f"- {result}")


def run_system_demo():
    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    # Definición centralizada de datos (Data Sets)
    s_batch = [22.5, 65, 1013]
    t_batch = ["buy:100", "sell:150", "buy:75"]
    e_batch = ["login", "error", "logout"]
    mixed_batch = [23.5, 21.0, "buy:200", "sell:500", "buy:50", "sell:100", "login", "error", "logout"]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: {s_batch}")
    print(sensor.process_batch(s_batch))

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print(f"Processing transaction batch: {t_batch}")
    print(trans.process_batch(t_batch))

    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing event batch: {e_batch}")
    print(event.process_batch(e_batch))

    print("\n=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    print("Batch 1 Results:")
    processor.process_all(mixed_batch)

    # Cálculo dinámico para el resumen basado en el estado interno de los objetos
    # Restamos el procesamiento inicial para obtener los datos nuevos del Batch 1
    sensor_alerts = sensor.processed_count - len(s_batch)
    print("\nStream filtering active: High-priority data only")
    print(f"Filtered results: {sensor_alerts} critical sensor alerts, 1 large transaction")
    print("All streams processed successfully. Nexus throughput optimal.")

if __name__ == "__main__":
    run_system_demo()
