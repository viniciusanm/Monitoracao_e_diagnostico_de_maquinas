def get_params_acc (mat):
    
    items_1 = mat.split('_')
    items_2 = items_1[len(items_1) - 1].split('.')
    items_2 = items_2[len(items_2) - 2]
    items_1 = items_1[:len(items_1) - 1]
    items = items_1 + [items_2]
    items = [int(y) for y in items]
    
    file = items[0]
    date = datetime.strptime(str(items[1]), '%Y%m%d')
    root_index = items[2]
    daily_passing = items[3]
    region = items[4]
    direction = items[5]
    sensor_num = items[6]
    
    return date, daily_passing, region, direction, sensor_num

def get_params_gps (mat):
    
    items_1 = mat.split('_')
    items_2 = items_1[len(items_1) - 1].split('.')
    items_2 = items_2[0][:1]
    items_1 = items_1[:len(items_1) - 1]
    items = items_1 + [items_2[0]]
    items = [int(y) for y in items]
    
    file = items[0]
    date = datetime.strptime(str(items[1]), '%Y%m%d')
    root_index = items[2]
    daily_passing = items[3]
    region = items[4]
    direction = items[5]
    
    return date, daily_passing, region, direction



def load_Data_Frame_acc (num_train, region_given, DateStart, DateEnd):
    
    df_date = pd.DataFrame()
    df_daily = pd.DataFrame()
    df_region = pd.DataFrame()
    df_direction = pd.DataFrame()
    df_trix = pd.DataFrame()
    df_triy = pd.DataFrame()
    df_triz = pd.DataFrame()
    df_front = pd.DataFrame()
    df_back = pd.DataFrame()
    df_1 = pd.DataFrame()
    df_2 = pd.DataFrame()
    df_acc = pd.DataFrame()
    
    
    if num_train == 4306:
        for mat in os.listdir(dataDir[0]):
            result = get_params_acc(mat)
            
            date = result[0]
            daily_passing = result[1]
            region = result[2]
            direction = result[3]
            sensor_num = result[4]
            
            if region == region_given and date >= DateStart and date <= DateEnd:
                
                try:
                    acc_1 = scipy.io.loadmat(dataDir[0]+mat)
                    
                    df_date = pd.DataFrame(data = [date], columns = ['Date'])
                    df_daily = pd.DataFrame(data = [daily_passing], columns = ['Daily_passing'])
                    df_region = pd.DataFrame(data = [region], columns = ['Region'])
                    df_direction = pd.DataFrame(data = [direction], columns = ['Direction'])
                    
                    if sensor_num == 1:
                        df_trix = pd.DataFrame(data = acc_1['save_var'], columns = ['Triaxial_x'])
                        
                    elif sensor_num == 2:
                        df_triy = pd.DataFrame(data = acc_1['save_var'], columns = ['Triaxial_y'])
                        
                    elif sensor_num == 3:
                        df_triz = pd.DataFrame(data = acc_1['save_var'], columns = ['Triaxial_z'])
                    
                    elif sensor_num == 4:
                        df_front = pd.DataFrame(data = acc_1['save_var'], columns = ['Front_cab_uni'])
                        
                    elif sensor_num == 5:
                        df_back = pd.DataFrame(data = acc_1['save_var'], columns = ['Back_cab_uni'])
                        
                        
                    df_1 = pd.concat([df_date, df_daily, df_region, df_direction, 
                                      df_trix, df_triy, df_triz, df_front, df_back], axis = 1)
        
                except:
                    acc_1 = h5py.File(dataDir[0]+mat, 'r').get('save_var')

                    df_date = pd.DataFrame(data = [date], columns = ['Date'])
                    df_daily = pd.DataFrame(data = [daily_passing], columns = ['Daily_passing'])
                    df_region = pd.DataFrame(data = [region], columns = ['Region'])
                    df_direction = pd.DataFrame(data = [direction], columns = ['Direction'])
                    
                    if sensor_num == 1:
                        df_trix = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Triaxial_x'])
                        
                    elif sensor_num == 2:
                        df_triy = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Triaxial_y'])
                        
                    elif sensor_num == 3:
                        df_triz = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Triaxial_z'])
                    
                    elif sensor_num == 4:
                        df_front = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Front_cab_uni'])
                        
                    elif sensor_num == 5:
                        df_back = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Back_cab_uni'])
                        
                    df_2 = pd.concat([df_date, df_daily, df_region, df_direction, 
                                      df_trix, df_triy, df_triz, df_front, df_back], axis = 1)
        

                df_acc = pd.concat([df_1, df_2], axis = 0, ignore_index = True)
            
                df_acc = df_acc.fillna(method = 'ffill')
                
                li_acc.append(df_acc)
                
        
        df_acc = pd.concat(li_acc, axis = 0, ignore_index = True)
        
        return df_acc

    elif num_train == 4313:
        for mat in os.listdir(dataDir[2]):
            result = get_params_acc(mat)
            
            date = result[0]
            daily_passing = result[1]
            region = result[2]
            direction = result[3]
            sensor_num = result[4]
            
            if region == region_given and date >= DateStart and date <= DateEnd:
                
                try:
                    acc_1 = scipy.io.loadmat(dataDir[2]+mat)
                    
                    df_date = pd.DataFrame(data = [date], columns = ['Date'])
                    df_daily = pd.DataFrame(data = [daily_passing], columns = ['Daily_passing'])
                    df_region = pd.DataFrame(data = [region], columns = ['Region'])
                    df_direction = pd.DataFrame(data = [direction], columns = ['Direction'])
                    
                    if sensor_num == 1:
                        df_trix = pd.DataFrame(data = acc_1['save_var'], columns = ['Triaxial_x'])
                        
                    elif sensor_num == 2:
                        df_triy = pd.DataFrame(data = acc_1['save_var'], columns = ['Triaxial_y'])
                        
                    elif sensor_num == 3:
                        df_triz = pd.DataFrame(data = acc_1['save_var'], columns = ['Triaxial_z'])
                    
                    elif sensor_num == 4:
                        df_front = pd.DataFrame(data = acc_1['save_var'], columns = ['Front_cab_uni'])
                        
                    elif sensor_num == 5:
                        df_back = pd.DataFrame(data = acc_1['save_var'], columns = ['Back_cab_uni'])
                        
                        
                    df_1 = pd.concat([df_date, df_daily, df_region, df_direction, 
                                      df_trix, df_triy, df_triz, df_front, df_back], axis = 1)
        
                except:
                    acc_1 = h5py.File(dataDir[0]+mat, 'r').get('save_var')

                    df_date = pd.DataFrame(data = [date], columns = ['Date'])
                    df_daily = pd.DataFrame(data = [daily_passing], columns = ['Daily_passing'])
                    df_region = pd.DataFrame(data = [region], columns = ['Region'])
                    df_direction = pd.DataFrame(data = [direction], columns = ['Direction'])
                    
                    if sensor_num == 1:
                        df_trix = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Triaxial_x'])
                        
                    elif sensor_num == 2:
                        df_triy = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Triaxial_y'])
                        
                    elif sensor_num == 3:
                        df_triz = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Triaxial_z'])
                    
                    elif sensor_num == 4:
                        df_front = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Front_cab_uni'])
                        
                    elif sensor_num == 5:
                        df_back = pd.DataFrame(data = np.array(acc_1).reshape(-1,1), columns = ['Back_cab_uni'])
                        
                    df_2 = pd.concat([df_date, df_daily, df_region, df_direction, 
                                      df_trix, df_triy, df_triz, df_front, df_back], axis = 1)
        

                df_acc = pd.concat([df_1, df_2], axis = 0, ignore_index = True)
            
                df_acc = df_acc.fillna(method = 'ffill')
                
                li_acc.append(df_acc)
                
        
        df_acc = pd.concat(li_acc, axis = 0, ignore_index = True)
        
        return df_acc    
    
    
def load_Data_Frame_gps (num_train, region_given, DateStart, DateEnd):

    df_date = pd.DataFrame()
    df_daily = pd.DataFrame()
    df_region = pd.DataFrame()
    df_direction = pd.DataFrame()
    df_aux = pd.DataFrame()
    df_gps = pd.DataFrame()
    
    
    if num_train == 4306:
        for mat in os.listdir(dataDir[1]):
            result = get_params_gps(mat)
            
            date = result[0]
            daily_passing = result[1]
            region = result[2]
            direction = result[3]
            
            if region == region_given and date >= DateStart and date <= DateEnd:
            
                gps_1 = scipy.io.loadmat(dataDir[1]+mat)
                
                df_date = pd.DataFrame(data = [date], columns = ['Date'])
                df_daily = pd.DataFrame(data = [daily_passing], columns = ['Daily_passing'])
                df_region = pd.DataFrame(data = [region], columns = ['Region'])
                df_direction = pd.DataFrame(data = [direction], columns = ['Direction'])
                
                df_aux = pd.DataFrame(data = gps_1['save_var_gps'], columns = ['Longitude', 'Latitude', 'Altitude', 'Velocidade', 'TimeStamp'])
    
                df_gps = pd.concat([df_date, df_daily, df_region, df_direction, df_aux], axis = 1)
        
                df_gps = df_gps.fillna(method = 'ffill')
            
                li_gps.append(df_gps)
                
        
        df_gps = pd.concat(li_gps, axis = 0, ignore_index = True)
        
        return df_gps
    
    
    elif num_train == 4313:
        for mat in os.listdir(dataDir[3]):
            result = get_params_gps(mat)
            
            date = result[0]
            daily_passing = result[1]
            region = result[2]
            direction = result[3]
            
            if region == region_given and date >= DateStart and date <= DateEnd:
            
                gps_1 = scipy.io.loadmat(dataDir[3]+mat)
                
                df_date = pd.DataFrame(data = [date], columns = ['Date'])
                df_daily = pd.DataFrame(data = [daily_passing], columns = ['Daily_passing'])
                df_region = pd.DataFrame(data = [region], columns = ['Region'])
                df_direction = pd.DataFrame(data = [direction], columns = ['Direction'])
                
                df_aux = pd.DataFrame(data = gps_1['save_var_gps'], columns = ['Longitude', 'Latitude', 'Altitude', 'Velocidade', 'TimeStamp'])
    
                df_gps = pd.concat([df_date, df_daily, df_region, df_direction, df_aux], axis = 1)
        
                df_gps = df_gps.fillna(method = 'ffill')
            
                li_gps.append(df_gps)
                
        
        df_gps = pd.concat(li_gps, axis = 0, ignore_index = True)
        
        return df_gps