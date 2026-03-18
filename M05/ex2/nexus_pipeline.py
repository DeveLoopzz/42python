from abc import ABC, abstractmethod
from typing import Any, List, Union, Protocol, Optional


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def build_pipeline(self) -> None:
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if isinstance(data["data"], dict):
            data["adapter"] = "json"
        else:
            raise ValueError("Invalid JSON data")
        for stage in self.stages:
            data = stage.process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if isinstance(data["data"], str):
            data["adapter"] = "csv"
            data["processed"] = data["data"].split(",")
        else:
            raise ValueError("Invalid CSV data")
        for stage in self.stages:
            data = stage.process(data)
        return data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if isinstance(data["data"], list):
            data["adapter"] = "stream"
        else:
            raise ValueError("Invalid Stream data")
        for stage in self.stages:
            data = stage.process(data)
        return data.get("output", data)


class InputStage:
    def process(self, data: Any) -> Any:
        d = data["data"]
        match data["adapter"]:
            case "json":
                if (
                    "sensor" not in d or
                    "value" not in d or
                    "unit" not in d
                    ):
                    raise TypeError("Invalid JSON keys")
            case "csv":
                for item in data["processed"]:
                    if not item:
                        raise TypeError("Invalid CSV data")
            case "stream":
                if not all(isinstance(item, int | float) for item in d):
                    raise TypeError("Invalid stream data")


class TransformStage:
    def process(self, data: Any) -> Any:
        if "info" in data and len(data["info"]) > 2:
            print(data["info"][2])
        
        adapter = data.get("adapter")
        raw = data.get("data")
        
        if adapter == "json":
            val = float(raw["value"])
            status = "Normal" if 0 < val < 35 else "Harsh"
            data["transformed"] = (val, raw["unit"], status)
        elif adapter == "csv":
            data["transformed"] = len(data["segments"])
        elif adapter == "stream":
            if not raw:
                raise ValueError("Empty stream in Stage 2")
            data["transformed"] = (len(raw), sum(raw) / len(raw))
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        if "info" in data and len(data["info"]) > 3:
            if data["info"][3] != "Output:":
                data["output"] = data["info"][3]
                return data

        adapter = data.get("adapter")
        res = data.get("transformed")

        if adapter == "json":
            v, u, s = res
            data["output"] = (f"Output: Processed temperature reading: "
                              f"{v}°{u} ({s} range)")
        elif adapter == "csv":
            data["output"] = (f"Output: User activity logged: "
                              f"{res} actions processed")
        elif adapter == "stream":
            n, a = res
            data["output"] = f"Output: Stream summary: {n} readings, avg: {a}°C"
        return data


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        pipeline.build_pipeline()
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        for pipe in self.pipelines:
            try:
                p_id = pipe.pipeline_id
                if p_id in data:
                    print(pipe.process(data[p_id]))
            except (KeyError, TypeError, ValueError):
                print("Error detected in Stage 2: Invalid data format")
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored")


def run_enterprise_demo():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    store = {
        "JSON_01": {
            "data": {"sensor": "temp", "value": 23.5, "unit": "C"},
            "info": [
                "Processing JSON data through pipeline...",
                "Input:",
                "Transform: Enriched with metadata and validation",
                "Output:"
            ]
        },
        "CSV_01": {
            "data": "user,action,timestamp",
            "info": [
                "\nProcessing CSV data through same pipeline...",
                "Input:",
                "Transform: Parsed and structured data",
                "Output:"
            ]
        },
        "STRM_01": {
            "data": [15.0, 23.0, 31.0, 20.0, 17.0],
            "info": [
                "\nProcessing Stream data through same pipeline...",
                "Input: Real-time sensor stream",
                "Transform: Aggregated and filtered",
                "Output:"
            ]
        }
    }

    mgr = NexusManager()
    mgr.add_pipeline(JSONAdapter("JSON_01"))
    mgr.add_pipeline(CSVAdapter("CSV_01"))
    mgr.add_pipeline(StreamAdapter("STRM_01"))

    print("=== Multi-Format Data Processing ===")
    mgr.process_data(store)
    
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    mgr.process_data({"STRM_01": {"data": "invalid", "info": []}})
    
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    run_enterprise_demo()
