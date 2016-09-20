# Before we start. 
# Make sure you have installed and attached the following packages:

library(pheatmap)
library(dplyr)
library(ggplot2)
library(reshape)
library(impute)
library(amap)

# To install the packages run the following commands
#install.packages("pheatmap")
#install.packages("dplyr")
#install.packages("ggplot2")
#install.packages("reshape")
#source("http://bioconductor.org/biocLite.R")
#biocLite("impute")
#install.packages("amap")

# Read in the data 
data_raw <- read.csv(file="data/RawDataPractice.csv",sep=",", row.names = 1)

# Meet your data

# Print out frst 6 lines of your data
head(data_raw)

# Structure of the object and information about the class, length and content of  each column
str(data_raw)

# summary statistics for each column
summary(data_raw)

# Returns a vector with the number of rows in the first element, and
# the number of columns as the second element.
# Place the name of your objects instead of "???".
dim(data_raw)

# Returns the number of columns.Place the name of your objects instead of "???".
ncol(data_raw)

# Returns the number of rows. Place the name of your objects instead of "???".
nrow(data_raw) 

# returns the column names and row mames.Place the name of your objects instead of "???".
colnames(data_raw)
rownames(data_raw)

## Plot raw data

# One good way of getting the first impression of how your data looks like is to visualize it.
# Heatmaps are great to get a general idea of the dataset that you are working with. 
# This type of visualization is well implemented in the package `pheatmap`.

# You can use the function `pheatmap()`. Use `?pheatmap()` to get more information about the arguments.
# Inspect the argument options that this function has.
# Now we are ready to create our first hetmap.

pheatmap(data_raw, cluster_rows = F, cluster_cols = F,scale = "none", 
         main="Raw gene expression")

## Challenge 1. 
# Using the help option change the fontsize on the figure. Replace "???" with the correct parameter. 
pheatmap(data_raw, cluster_rows = F, cluster_cols = F,scale = "none", ???, 
         main="Raw gene expression")

## Plot distributions

# Next we will "melt" an object into a form suitable for easy plotting.
# Let's create a function that adds the type(group) of our samples (H, PG1, PG2) to the data and melts it.

meltmydata<-function(df){
  # Transpose
  dt=t(df)
  
  # Convert to data.frame
  dt=as.data.frame(dt)
  
  # Bind the column with sample names
  dt=cbind(dt, sample = rownames(dt))
  
  # Change the type of the column
  dt$sample=as.character(dt$sample)
  
  # Remove sample number 
  dt$sample <- gsub("0.*","", dt$sample)
  
  # Melt the data
  data_melt <- melt(dt)
  
  # Change the names of the columns
  colnames(data_melt)=c("Group","Gene","Expression")
  return(data_melt)
}

data_raw_melt <- meltmydata(data_raw)
head(data_raw_melt)

# Currently we can notice that there are a lot of missing values in the data.
# However, since the range of the expression values varies a lot, we can't make any
# conclusions about the dataset just by looking at the heatmap.

# To see how the expression values of each gene is distributed in each group of patients and healthy individuals,
# we will use R package `ggplot2` and in particular function `geom_density()`.

# Plot the distributions
ggplot(data_raw_melt, aes(x=Expression))+
facet_wrap(~Gene, scales = "free" )+
theme_bw()+
geom_density(aes(group=Group, colour=Group,fill=Group), alpha=0.5)+
ggtitle("Density plot of gene expression")

# Impute missing values

# Missing values in the datata can appear due to the different technical errors, human errors etc.
# There are essentially tree ways of handeling missing values. Can you recall them from the lecture?

# In this tutorial we will use k-nearest neighbour algorithm to impute the missing values in our data.
# For this purpose download and attach "impute" package  from Bioconductor http://www.bioconductor.org/packages/release/bioc/html/impute.html

#Function `impute.knn()` doesn't take dataframe as an argumet.
#Let's change it to matrix. 
#To convert our dataframe from matrix we will use function `as.matrix()`

# Create new dataframe. Store the imputed values there.
data_raw<-as.matrix(data_raw)
data_imp <- impute.knn(data_raw ,k = 3, rowmax = 0.8, colmax = 0.8, maxp = 1500, rng.seed=362436069)

## Challenge 2.
# Impute the data using 4 KNN and visualize the results using heatmap.
data_raw<-as.matrix(data_raw)
data_imp <- impute.knn(data_raw ,???, rowmax = 0.8, colmax = 0.8, maxp = 1500, rng.seed=362436069)

## Challenge 3. Plot the imputed data using pheatmap(). Name the plot "Gene expression after imputation".
pheatmap(???)


## Normalize  and scale your data

# In order to remove technical variance in the data and make the samples more comparable we will normalize and standardise it.
# The methods of normalization is highly specific to the experimental origin of the data and it's properties.
# In this tutorial we will logarithmize, scale and center the data based on the mean and standard deviation of the expression of each individual gene(row).

# Logarithmize gene expression
data_log <- log2(data_imp$data)

# Center and scale data by row
scale_rows <- function(x){
  m = apply(x, 1, mean, na.rm = T)
  s = apply(x, 1, sd, na.rm = T)
  return((x - m) / s)
}
data_norm <- scale_rows(data_log)

## Challenge 4. Plot scaled data using pheatmap(). Name the plot "Gene expression after normalization".
pheatmap(???)

# Save your processed data to a file using special R compressed data file format .RData or .csv file to access it later.

save(data_norm,file="results/RawData.rds")
write.table(data_norm, file="results/data_processed.csv",sep=",",row.names=T, quote=F)

## Handle outliers

#You can detect the outliers in the distribution of your data by looking at the boxplots.
#In case you decided to filter out outliers interquartile rate can be applied as a filtering criterion.

data_norm_melt <- meltmydata(data_norm)

ggplot(data_norm_melt ,aes(factor(Group),Expression))+
  facet_wrap(~Gene,scales="free_y")+
  theme_bw()+
  theme_bw(base_size = 6)+
  geom_boxplot(outlier.shape=NA,fatten = 0.2,lwd=0.2)+
  geom_jitter(width = .7,size =0.01,aes(colour = Group))+
  scale_color_manual(values = c("#00ba38","#d4170a","#00ebf2"))+
  theme(text = element_text(size=6),
        axis.text.x = element_text(size=6),
        legend.text=element_text(size=6),legend.position = "none",
        axis.title.x = element_blank(),axis.title.y = element_blank()
  ) 


## PCA

data.pca=t(data_norm)
my_pca=prcomp(data.pca, scale=T, center=T)
imp=summary(my_pca)$importance

# Plot the variance covered by each PC
barplot(imp[2,]*100,ylab="Persentage of variance", xlab="Principal Components",main = "Variance explained by individual PC", col="cyan3")

# Plot with ggplot and color samples by group 
my_pca <- data.frame(my_pca$x)

# Add group annotations
my_pca <- cbind(my_pca, Group = rownames(data.pca))

# Remove the indexes
my_pca$Group <- gsub("H.*","Healthy individuals",my_pca$Group)
my_pca$Group <- gsub("PG1.*","Patients in group 1",my_pca$Group)
my_pca$Group <- gsub("PG2.*","Patients in group 2",my_pca$Group)


# Plot PCA with ggplot2
ggplot(my_pca, aes(x = PC1, y = PC2, colour = Group)) + 
  theme_bw(base_size = 8) + 
  geom_point()+
  labs(x = 'PC1', y = 'PC2') + 
  scale_colour_manual(values = c("#00ba38","#d4170a","#00ebf2")) + 
  theme(
    legend.position = c(1, 0),
    legend.direction = "vertical",
    legend.justification = c(1, 0)
  )+
  stat_ellipse()


## Cluster your data

## K-means clustering
#First of all you want to understand how many K(s) to select.
#To do that you could use so called "elbow" rule.
#The appropriate number of clusters can be selected based on the the sum of squared error (SSE) for a number of cluster solutions.
#SSE is defined as the sum of the squared distance between each member of a cluster and its cluster centroid. 
# An appropriate cluster solution is the solution at which the reduction in SSE decreases dramatically. 
#This produces a bending point in the plot of SSE against cluster solutions. 

wss <-  (nrow(data_norm)-1)*sum(apply(data_norm,2,var))
for (i in 2:10) wss[i] <- sum(kmeans(data_norm, 
                                     centers=i)$withinss)
plot(1:10, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")


# Let's select number of clusters 3 and run K-means clustering on our data.

s=set.seed(1234)
km=Kmeans(data_norm,3,iter.max = 100500, nstart =50, method = "correlation")

# Explore the structure
head(km)

# Plot the results
pheatmap(data.frame(km$centers) , cluster_rows=T, cluster_cols=F, scale = "none",
clustering_distance_rows = "correlation",
border_color = "grey60",
main="Clustered gene expression after normalization")


# We can also visualise clustering results just by using heatmap.
pheatmap(data_norm, cluster_rows=T, cluster_cols=F, scale = "none",
clustering_distance_rows = "correlation",
kmeans_k = 3,
border_color = "grey60",
main="Gene expression after normalization")


## Hierarchical clustering

hc.data = hcluster(data_norm, method = "euclidean", diag = FALSE, upper = FALSE,
link = "complete", members = NULL, nbproc = 2,
doubleprecision = TRUE)

plot(hc.data)
# Split into 3 clusters
ct=cutree(hc.data, k=3)
sort(ct)
save(ct, hc.data, file = "results/hc.RData")



## Extract knowledge

## Gene Ontology cluster annotations

#After you have identified the clusters, you can characterise the genes that are located in each of them.
#We can identify the biological processed that they are involved in using package `GOsummaries`
#or using a web-tool gProfiler http://biit.cs.ut.ee/gprofiler/.

library(GOsummaries)
# Get gene names in each of the cluster
g1=as.character(names(sort(ct[ct==1])))
g2=as.character(names(sort(ct[ct==2])))
g3=as.character(names(sort(ct[ct==3])))

write.table(g1, file="results/genelist.txt",sep="\t",row.names = F,col.names = F, quote = F)

# Add annotations
gl=list(Cluster1 = g1, Cluster2 = g2, Cluster3 = g3)
gs = gosummaries(gl)
plot(gs, fontsize = 8)

# Create samples' annotation
Groups=colnames(data_norm)
Groups <- gsub("H.*","Healthy individuals",Groups)
Groups <- gsub("PG1.*","Patients in group 1",Groups)
Groups <- gsub("PG2.*","Patients in group 2",Groups)

my_annotation=cbind(Groups, Groups)
rownames(my_annotation)=colnames(data_norm)
my_annotation=as.data.frame(my_annotation[,1])
colnames(my_annotation)="Groups"
gs_exp = add_expression.gosummaries(gs, exp = data_norm,
                                    annotation = my_annotation)
plot(gs_exp, fontsize = 8, classes = "Groups")




