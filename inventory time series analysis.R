k <- 60
for (j in 1:6) {
  k <- k+1
  y <- ts(elecequip, frequency = 12, start = c(1996,1), end = c(2001,j))
  y <- tsclean(y,replace.missing = TRUE, lambda = 'auto')
  y_de <- stl(y,"periodic")
  y1 <-y-y_de$time.series[,2]
  kp <- kpss.test(y1,null = c('Trend'))
  if (kp$p.value > 0.05){
    sprintf("have no evidence that it is not trend stationary for train data from 1996 1 to 2001 %i",j)
  }
  fit<-auto.arima(y1)
  y_pred<-forecast(fit,5,level = 90)
  y_real<-y_pred$mean+y_de$time.series[k,2]
  write(y_real, file = "out_mean2.csv", append = TRUE, sep = ",")
  write(y-y_de$time.series[,2]-y_pred$fitted, file = "out_error2.csv", append = TRUE, sep = ",")
}

#have no evidence that it is not trend stationary.


