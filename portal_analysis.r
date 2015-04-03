## Load Panel Data
panel.data <- read.csv(".../socrata panel data.csv")

summary(panel.data)

## GLM Poisson 1 (rows.accessed.total)
model1 <- glm(log(rows.accessed.total) ~ log(rows.created) + log(rows.deleted) + log(bytes.in) + log(bytes.out) + log(disk.usage)
              + factor(month) + factor(school), family=poisson(),
              data = panel.data)

summary(model1)
par(mfrow=c(2,2))
plot(model1)

## Calculate Robust Standard Errors for Model 1
library(sandwich)
library(lmtest)

cov.m1 <- vcovHC(model1, type="HC2")
std.err <- sqrt(diag(cov.m1))
r.est <- cbind(Estimate= coef(model1), "Robust SE" = std.err,
               "Pr(>|z|)" = 2 * pnorm(abs(coef(model1)/std.err), lower.tail=FALSE),
               LL = coef(model1) - 1.96 * std.err,
               UL = coef(model1) + 1.96 * std.err)

print(r.est)

## GLM Poisson 2 (rows.loaded.total)
model2 <- glm(log(rows.loaded.total) ~ log(rows.created) + log(rows.deleted) + log(bytes.in) + log(bytes.out) + log(disk.usage)
              + factor(month) + factor(school), family=poisson(),
              data = panel.data)

summary(model2)
par(mfrow=c(2,2))
plot(model2)

## Calculate Robust Standard Errors for Model 2
library(sandwich)
library(lmtest)

cov.m2 <- vcovHC(model2, type = "HC2")
std.err <- sqrt(diag(cov.m2))
r.est2 <- cbind(Estimate= coef(model2), "Robust SE" = std.err,
               "Pr(>|z|)" = 2 * pnorm(abs(coef(model2)/std.err), lower.tail=FALSE),
               LL = coef(model2) - 1.96 * std.err,
               UL = coef(model2) + 1.96 * std.err)

print(r.est2)


## Visualizations

library(ggplot2)
data <- panel.data
data <- within(data, {
  portal <- factor(portal)
  month <- factor(month)
  
})

## Rows.accessed.total for each portal across 36 months
library(ggplot2)
p <- ggplot(data = data, aes(x = month, y = log(rows.loaded.total), group = portal))

p + geom_line() + stat_smooth(aes(colour= factor(portal)), method = "glm", family="poisson") + stat_summary(aes(group = portal),
geom = "point", fun.y = median, shape = 17, size = 0) + facet_wrap( ~ portal)

## All rows.loaded
p1a <- ggplot(data = data, aes(x = month, y= log(rows.loaded.api), y2=log(rows.loaded.download), y3=log(rows.loaded.rss), y6=log(rows.loaded.print), group = portal))

p1a + labs(x="Month", y="Log Count", title="Rows-Loaded, Disaggregated") + theme(legend.title=element_blank()) + theme(axis.text.x=element_text(angle=90, size=10, vjust=0.5)) + 
  geom_line(aes(y=log(rows.loaded.api), colour= "rows.loaded.api")) + geom_line(aes(y = log(rows.loaded.download), colour = "rows.loaded.download")) +
  geom_line(aes(y = log(rows.loaded.rss), colour="rows.loaded.rss")) + geom_line(aes(y = log(rows.loaded.print), colour="rows.loaded.print")) +
  facet_wrap( ~ portal)

## All rows.accessed
p1b <- ggplot(data = data, aes(x = month, y= log(rows.accessed.api), y2=log(rows.accessed.download), y3=log(rows.accessed.rss), y6=log(rows.accessed.print), group = portal))

p1b + labs(x="Month", y="Log Count", title="Rows-Accessed, Disaggregated") + theme(legend.title=element_blank()) + theme(axis.text.x=element_text(angle=90, size=10, vjust=0.5)) +
  geom_line(aes(y=log(rows.accessed.api), colour= "rows.accessed.api")) + geom_line(aes(y = log(rows.accessed.download), colour = "rows.accessed.download")) +
  geom_line(aes(y = log(rows.accessed.rss), colour="rows.accessed.rss"))+ geom_line(aes(y = log(rows.accessed.print), colour="rows.accessed.print")) +
  facet_wrap( ~ portal)

## Aggregate rows.accessed
p1c <- ggplot(data = data, aes(x = month, y= log(rows.accessed.total), group = portal))

p1c + labs(x="Month", y="Log Count", title="Rows-Accessed, Aggregated") + theme(legend.title=element_blank()) + theme(axis.text.x=element_text(angle=90, size=10, vjust=0.5)) + 
  geom_line(aes(y=log(rows.accessed.total), colour= "rows.accessed.total")) + facet_wrap( ~ portal)

## Aggregate rows.accessed
p1d <- ggplot(data = data, aes(x = month, y= log(rows.loaded.total), group = portal))

p1d + labs(x="Month", y="Log Count", title="Rows-Loaded, Aggregated") + theme(legend.title=element_blank()) + theme(axis.text.x=element_text(angle=90, size=10, vjust=0.5)) + 
  geom_line(aes(y=log(rows.loaded.total), colour= "rows.loaded.total")) + facet_wrap( ~ portal)

## Rows.created, rows.deleted, rows.accessed.api 
p2 <- ggplot(data = data, aes(x = month, y= log(rows.created), y2=log(rows.deleted), y3=log(rows.accessed.api), group = portal))

p2 + geom_line(aes(y=log(rows.accessed.api), colour= "rows.accessed.api")) + geom_line(aes(y = log(rows.created), colour = "rows.created")) + geom_line(aes(y = log(rows.deleted), colour="rows.deleted")) +
facet_wrap( ~ portal)

## Bytes.in vs bytes.out
p3 <- ggplot(data = data, aes(x = month, y= log(bytes.in), y2=log(bytes.out), group = portal))

p3 + geom_line(aes(y = log(bytes.in), colour = "bytes.in")) + geom_line(aes(y = log(bytes.out), colour="bytes.out")) +
  facet_wrap( ~ portal)

## Disk.usage

p4 <- ggplot(data = data, aes(x = month, y= log(disk.usage), group = portal))

p4 + geom_line(aes(y = log(disk.usage), colour = "disk.usage")) +
  facet_wrap( ~ portal)

## All independent variables in model
p5 <- ggplot(data = data, aes(x = month, y= log(rows.created), y2=log(rows.deleted), y3=log(bytes.in), y4=log(bytes.out), y5=log(disk.usage), group = portal))

p5 + labs(x="Month", y="Log Count", title="Independent Variables") + theme(legend.title=element_blank()) + theme(axis.text.x=element_text(angle=90, size=10, vjust=0.5)) +
  geom_line(aes(y = log(rows.created), colour = "rows.created")) + geom_line(aes(y = log(rows.deleted), colour="rows.deleted")) +
  geom_line(aes(y=log(bytes.in), colour= "bytes.in")) + geom_line(aes(y=log(bytes.out), colour= "bytes.out")) + geom_line(aes(y=log(disk.usage), colour= "disk.usage")) + facet_wrap( ~ portal) + theme(legend.title=element_blank())

