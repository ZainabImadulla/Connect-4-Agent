
''' 
    def in_a_row_horizontal(self, player, num):
        total_num_in_row = 0
        count = 0
        empty_space = 0
        starting_empty_space = 0
        for row in range(6):
            for i in range(7):
                print(str(row) + " , " + str(i) + " = " + str(self.board[row][i]))
                if self.board[row][i] == player:
                    count += 1
                    if count == num and empty_space >= 1:
                        print("count point: total count increased at row " + str(row) + " and col " + str(i))
                        print("in column " + str(i))
                        print("count " + str(count))
                        print("empty space " + str(empty_space))
                        total_num_in_row += 1
                        count = 1
                        empty_space = 0
                        
                elif self.board[row][i] == (3 - player):
                    count = 0
                    empty_space = 0
                elif self.board[row][i] == 0:
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count == num and empty_space == 1:
                        print("space point: total count increased at row " + str(row) + " and col " + str(i))
                        print("in column " + str(i))
                        print("count " + str(count))
                        print("empty space " + str(empty_space))
                        total_num_in_row += 1
                        count = 0
            empty_space = 0
            count = 0
        return total_num_in_row
    
    def in_a_row_vertical(self, player, num):
        total_num_in_row = 0
        count = 0
        empty_space = 0
        for column in range(7) :
            for i in range(6):
            # print(str(row) + " , " + str(i) + " = " + str(self.board[row][i]))
                if self.board[i][column] == player:
                    count += 1
                    if count == num and empty_space >= 1:
                        print("reached")
                        total_num_in_row += 1
                        count = 1
                        empty_space = 0
                elif self.board[i][column] == (3 - player):
                    count = 0
                    empty_space = 0
                elif self.board[i][column] == 0:
                    empty_space += 1
                    if empty_space >= 2:
                        count = 0
                    if count == num and empty_space >= 1:
                        print("reached")
                        total_num_in_row += 1
                        count = 0
            empty_space = 0
            count = 0
            #print("in column " + str(i))
            #print("count " + str(count))
            #print("empty space " + str(empty_space))
        return total_num_in_row
        

        
        def testInARowHorizontal(self):
            
            
            self.assertEqual(self.board10.in_a_row_horizontal( 1, 2), 2)
            
            self.assertEqual(self.board11.in_a_row_horizontal( 2, 2), 2)
            self.assertEqual(self.board10.in_a_row_horizontal( 1, 3), 1)
            self.assertEqual(self.board10.in_a_row_horizontal( 1, 2), 2)

            self.assertEqual(self.board10.in_a_row_horizontal( 2, 2), 0)
        
            self.assertEqual(self.board5.in_a_row_horizontal( 2, 2), 3)
            self.assertEqual(self.board9.in_a_row_horizontal(1, 3), 1)

            self.assertEqual(self.board9.in_a_row_horizontal( 2, 3), 2)
            

        def testInARowVertical(self):
            self.assertEqual(self.board9.in_a_row_vertical( 2,2), 0)
            self.assertEqual(self.board9.in_a_row_vertical(1 ,2), 1)
            self.assertEqual(self.board9.in_a_row_vertical(2,2), 0)
            self.assertEqual(self.board9.in_a_row_vertical( 2, 3), 1)


        '''
        