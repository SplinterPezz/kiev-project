import React, { Component } from "react";
import Chart from "react-apexcharts";
import '../App.css';
import { Card, InputNumber, Button, Space, message } from 'antd';
import { chartService } from '../services/chart.service';
import { chartOption } from '../utils/chart.option';

const default_days = 19;
const articles_url = "death-article";
const death_and_articles_url = "death-and-article";
const importedOptions = chartOption.getSplittedChart();


class ArticleDeathChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            articleChart: {
                options: {},
                series: []
            },
            deathAndArticleChart: {
                options: {},
                series: []
            },
            days: default_days,
            ...importedOptions
        };
    }

    componentDidMount() {
        this.getArticlesDeathChart(articles_url, default_days);
        this.getArticlesDeathChart(death_and_articles_url, default_days);
    }

    setDays(days) {
        if(days !== undefined){
            this.setState({
                ...this.state,
                days: days
            });
            this.getArticlesDeathChart(articles_url, days);
            this.getArticlesDeathChart(death_and_articles_url, days);
        }
        
    }



    getArticlesDeathChart = (charType, days) => {
        chartService.getArticlesDeath(charType, days).then(res => {
            if (charType === articles_url) {
                this.setState({
                    ...this.state,
                    articleChart: {
                        options: {
                            chart: this.state.chart,
                            responsive: this.state.responsive,
                            plotOptions: this.state.plotOptions,
                            xaxis: res['xaxis'],
                            fill: this.state.fill
                        },
                        series: res['series']
                    },

                });
            }
            else {
                this.setState({
                    ...this.state,
                    deathAndArticleChart: {
                        options: {
                            chart: this.state.chart,
                            responsive: this.state.responsive,
                            plotOptions: this.state.plotOptions,
                            xaxis: res['xaxis'],
                            fill: this.state.fill
                        },
                        series: res['series']
                    },

                });
            }

        },
        error=>{
            console.log('ERROR',error)
            message.error(`An error occurred during getting articles death chart`);
        });
    }


    render() {
        return (
            <div className="site-card-border-less-wrapper mt-5">
                <Card title="Articles about Death" bordered={false} extra={
                    <Space>
                        <InputNumber min={1} max={99} value={this.state.days} onChange={(e) => this.setDays(e)} />
                        <Button type="primary" onClick={() => { this.setDays(default_days); }}>
                            Reset
                        </Button>
                    </Space>
                }>
                    <div className="app">
                        <div className="row">
                            <div className="mixed-chart col-12 col-lg-6">
                                <Chart
                                    height={"400 px"}
                                    options={this.state.articleChart.options}
                                    series={this.state.articleChart.series}
                                />
                            </div>
                            <div className="mixed-chart  col-12 col-lg-6">
                                <Chart
                                    height={"400 px"}
                                    options={this.state.deathAndArticleChart.options}
                                    series={this.state.deathAndArticleChart.series}
                                />
                            </div>
                        </div>
                    </div>
                </Card>
            </div>
        );
    }
}


export default ArticleDeathChart;
