# Estimator 会封装下列操作：
import tensorflow as tf
estimator = tf.estimator.LinearClassifier(feature_columns=[population, crime_rate, median_education])
# 训练
# 评估
# 预测
# 导出以供使用