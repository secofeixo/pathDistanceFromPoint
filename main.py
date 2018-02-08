# -*- coding: utf-8 -*-
# import logging

# # configure the logging system with default values
# logging.basicConfig(format='%(asctime)s. %(levelname)s. %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
# loggerGS = logging.getLogger()

class cell(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return "Cell. Row: " + str(self.row) + ". Col:" + str(self.col)

    def getNeighbours(self, matrix, rowsMatrix, colsMatrix):
        arNeighbours = []

        iInitRow = self.row - 1
        if (iInitRow < 0):
            iInitRow = 0
        iFinalRow = self.row + 1
        if (iFinalRow > rowsMatrix - 1):
            iFinalRow = rowsMatrix - 1

        iInitCol = self.col - 1
        if (iInitCol < 0):
            iInitCol = 0
        iFinalCol = self.col + 1
        if (iFinalCol > colsMatrix - 1):
            iFinalCol = colsMatrix - 1

        for iNewRow in range(iInitRow, iFinalRow + 1):
            for iNewCol in range(iInitCol, iFinalCol + 1):
                # jump the same cell
                if (iNewCol == self.col) and (iNewRow == self.row):
                    continue
                # jump diagonal cells
                if (iNewCol != self.col) and (iNewRow != self.row):
                    continue

                if (matrix[iNewRow][iNewCol] == 1):
                    newcell = cell(iNewRow, iNewCol)
                    arNeighbours.append(newcell)

        return arNeighbours

class matrix(object):
    def __init__(self):
        self.cols = 9
        self.rows = 6
        # matrix which store the final result. The defualt value 999999 indicates not set
        self.resultMatrix = [[9999999 for x in range(self.cols)] for y in range(self.rows)]
        # Matrix that represents the cells
        self.matrix = [[0 for x in range(self.cols)] for y in range(self.rows)]

        # self.matrix[row][col] = 1 to set that that cell is available
        # self.matrix[row][col] != 1 to set that that cell is unavailable
        self.matrix[0][1] = 1
        self.matrix[1][1] = 1
        self.matrix[2][1] = 1
        self.matrix[5][1] = 1
        self.matrix[2][2] = 1
        self.matrix[5][2] = 1
        self.matrix[1][3] = 1
        self.matrix[2][3] = 1
        self.matrix[3][3] = 1
        self.matrix[4][3] = 1
        self.matrix[5][3] = 1
        self.matrix[1][4] = 1
        self.matrix[4][4] = 1
        self.matrix[1][5] = 1
        self.matrix[4][5] = 1
        self.matrix[1][6] = 1
        self.matrix[2][6] = 1
        self.matrix[3][6] = 1
        self.matrix[4][6] = 1
        self.matrix[4][7] = 1
        self.matrix[4][8] = 1
        self.matrix[5][8] = 1

    def getPath(self, cell, iStep):
        if not ((cell.row < self.rows) and (cell.col < self.cols)):
            print (cell, "out of bounds")
            return

        if (self.matrix[cell.row][cell.col] != 1):
            print (cell, "not valid")
            return

        self.resultMatrix[cell.row][cell.col] = iStep

        iStep += 1
        # loggerGS.debug("getPath. Step %f. Cell: %s", iStep, cell)
        arNeighbours = cell.getNeighbours(self.matrix, self.rows, self.cols)
        for cellNeighbour in arNeighbours:
            distanceNeighbour = self.resultMatrix[cellNeighbour.row][cellNeighbour.col]
            if (distanceNeighbour > iStep):
                self.getPath(cellNeighbour, iStep)

    def showResultMatrix(self):
        for x in range(self.rows):
            print ('[',' '.join('{:^7}'.format(k) for k in self.resultMatrix[x]),']')
            # print (self.resultMatrix[x])

    def showInputMatrix(self):
        for x in range(self.rows):
            print ('[',' '.join('{:^3}'.format(k) for k in self.matrix[x]),']')

def main():
    iStep = 0
    # set the init cell
    initCell = cell(4, 3)
    print ("Init ", initCell)
    # loggerGS.info("InitCell %s.", initCell)
    matrixObj = matrix()
    matrixObj.getPath(initCell, iStep)
    print ("Input matrix")
    print ("--------------------------")
    matrixObj.showInputMatrix()
    print ("==========================")
    print ("Result matrix")
    print ("--------------------------")
    matrixObj.showResultMatrix()

if __name__ == "__main__":
    main()
