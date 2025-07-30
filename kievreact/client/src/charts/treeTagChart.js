import React, { Component } from "react";
import Chart from "react-apexcharts";
import '../App.css';
import { Card, InputNumber, Button, Space, message } from 'antd';
import { chartService } from '../services/chart.service';
import { chartOption } from '../utils/chart.option';

const default_days = 5;
const importedOptions = chartOption.getTreeMapChart();

class TreeTagChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            series: [],
            options: {
                ...importedOptions,
            },
            days: default_days
        };
    }

    componentDidMount() {
        this.getTotalDeathChart(default_days);
    }

    setDays(days) {
        if(days !== undefined){
            this.setState({
                ...this.state,
                days: days
            });
            this.getTotalDeathChart(days);
        }
        
    }

    getTotalDeathChart = (days) => {
        chartService.getTreeTag(days).then(res => {
            this.setState({
                ...this.state,
                series: res,
            });
        },
        error=>{
          console.log('ERROR',error)
          message.error(`An error occurred during getting tree tag chart`);
        });
    }

    render() {
        return (
            <div className="site-card-border-less-wrapper mt-4">
                <Card title="Total deaths and injureds" bordered={false} extra={
                    <Space>
                        <InputNumber min={1} max={99} value={this.state.days} onChange={(e) => this.setDays(e)} />
                        <Button type="primary" onClick={() => { this.setDays(default_days); }}>
                            Reset
                        </Button>
                    </Space>
                }>
                    <div className="app">
                        <div className="row">
                            <div className="mixed-chart">
                                <Chart
                                    height={"500 px"}
                                    options={this.state.options}
                                    series={this.state.series}
                                    type="treemap"
                                />
                            </div>
                        </div>
                    </div>
                </Card>
            </div>
        );
    }
}


export default TreeTagChart;
