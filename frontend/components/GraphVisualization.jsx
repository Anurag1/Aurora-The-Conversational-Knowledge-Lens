import * as d3 from "d3";
import { useEffect, useRef } from "react";

export default function GraphVisualization({ data }) {
  const ref = useRef();
  useEffect(() => {
    const svg = d3.select(ref.current);
    svg.selectAll("*").remove();
    const simulation = d3.forceSimulation(data.nodes)
      .force("link", d3.forceLink(data.links).distance(100))
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter(400, 250));
    const link = svg.selectAll("line").data(data.links).enter().append("line").attr("stroke", "#aaa");
    const node = svg.selectAll("circle").data(data.nodes).enter().append("circle").attr("r", 10).attr("fill", "#4CAF50");
    simulation.on("tick", () => {
      link.attr("x1", d => d.source.x).attr("y1", d => d.source.y).attr("x2", d => d.target.x).attr("y2", d => d.target.y);
      node.attr("cx", d => d.x).attr("cy", d => d.y);
    });
  }, [data]);
  return <svg ref={ref} width={800} height={500}></svg>;
}
