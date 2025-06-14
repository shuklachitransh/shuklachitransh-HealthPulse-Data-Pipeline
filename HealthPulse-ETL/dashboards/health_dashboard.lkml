explore: health_metrics {
  view: health_metrics {
    dimension: user_id {}
    dimension: timestamp { type: time }
    measure: avg_heart_rate { type: average, sql: ${heart_rate} }
    measure: total_steps { type: sum, sql: ${steps} }
    ...
  }
}