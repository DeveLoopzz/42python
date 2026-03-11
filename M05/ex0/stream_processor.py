from abc import ABC, abstractmethod
from typing import Any, List

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    
    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        result = (
            f"Processed {len(data)} numeric values, sum={sum(data)}, " 
            f"avg={sum(data)/ len(data):.1f}"
        )
        return self.format_output(result)

    def validate(self, data: Any) ->bool:
        return (
            isinstance(data, list) and
            all(isinstance(item, (int, float)) for item in data)
        )


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        result = (
            f"Processed text: {len(data)} "
            f"characters, {len(data.split())}"
        )
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        if "Error" in data:
            result: str = "ERROR level detected: connection timeout"
        else:
            result: str = "INFO level detected: System ready"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f"[ALERT] {result}"
        else:
            return f"[INFO] {result}"

def polymorphic_demo():
    processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(), LogProcessor()]
    dataset: List[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through stame interface...")
    for i, (proc, data) in enumerate(zip(processors, dataset)):
        try:
            result = proc.process(data)
            print(f"Result {i + 1}: {result}")
        except ValueError as e:
            print(f"Error processing data: {e}")
    print("Foundation systems online. Nexus ready for advanced streams.")

def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    print("Initializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    num_proc = NumericProcessor()
    if num_proc.validate(numeric_data):
        print("Validation: Numeric data verified")
        print(num_proc.process(numeric_data))

    print("Initializing Text Processor...")
    print(f"Processing data: \"{text_data}\"")
    txt_proc = TextProcessor()
    if txt_proc.validate(text_data):
        print("Validation: Text data verified")
        print(txt_proc.process(text_data))

    print("Initializing Log Processor...")
    print(f"Processing data: \"{log_data}\"")
    log_proc = LogProcessor()
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        print(log_proc.process(log_data))

if __name__ == "__main__":
    main()
    polymorphic_demo()
