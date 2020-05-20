library(tidyverse)
library(ggpubr)

N = 10000 # number of die rolls (aka precision and runtime)
d = 20 # number of sides on the die

rollsREG <- NULL
rollsAOD <- NULL
rollsDOA <- NULL

for(i in 1:N){
        roll4 <- sample.int(n = 20, size = 4, replace = TRUE)
        rollsREG <- append(rollsREG, roll4)
        rollsAOD <- append(rollsAOD, max(min(roll4[1], roll4[2]), min(roll4[3], roll4[4])))
        rollsDOA <- append(rollsDOA, min(max(roll4[1], roll4[2]), max(roll4[3], roll4[4])))
}

print(c('last rolls', roll4))
print(c('regular expected roll', mean(rollsREG)))
print(c('advantage of disadvantage expected roll', mean(rollsAOD)))
print(c('disadvantage of advantage expected roll', mean(rollsDOA)))

rollsREG <- as.data.frame(rollsREG)
rollsAOD <- as.data.frame(rollsAOD)
rollsDOA <- as.data.frame(rollsDOA)

pdf <- ggplot() +
        stat_bin(data = rollsREG, 
                 aes(rollsREG, ..density..), 
                 geom="step", bins = 20, color = "blue") + 
        stat_bin(data = rollsAOD, 
                 aes(rollsAOD, ..density..), 
                 geom = "step", bins = 20, color = "orange") +
        stat_bin(data = rollsDOA, 
                 aes(rollsDOA, ..density..), 
                 geom = "step", bins = 20, color = "green") +
        theme_classic() + 
        labs(x = "Result of Roll", y = "Probability of Result", title = "PDF")


revcdf <- ggplot() +
        stat_ecdf(data = rollsREG, 
                  aes(x = rollsREG, y = 1- ..y.., color = "rollsREG")) +
        stat_ecdf(data = rollsAOD, 
                  aes(x = rollsAOD, y = 1- ..y.., color = "rollsAOD")) + 
        stat_ecdf(data = rollsDOA, 
                  aes(x = rollsDOA, y = 1- ..y.., color = "rollsDOA")) +
        theme_classic() + 
        labs(x = "Result of Roll", y = "Reverse Cumulative Probability", title = "Reverse CDF") +
        scale_color_manual(name = "", values = c( "rollsREG" = "blue", "rollsAOD" = "orange", "rollsDOA" = "green"),
                           labels = c("Advantage of Disadvantage", "Disadvantage of Advantage", "d20"))

# plot together
p <- ggarrange(pdf, revcdf, nrow=1, common.legend = TRUE, legend="bottom")

ggsave(filename = "extracredit.png", plot = p)

