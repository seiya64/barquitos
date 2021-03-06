#include <cstdio>
#include <cstdlib>
#include <ctime>

#define LADOTAB 10
#define BARCOS	5

#define HORIZONTAL 0
#define VERTICAL   1

int numero_aleatorio_entre(int minimo, int maximo) {
	return ((rand() % (maximo - minimo + 1)) + minimo);
}

bool colision (int **tablero, int x, int y, int ori, int tam) {
	bool found = false;
	
	for (int j = 0; (j < tam) && (!found); j++) {
		if (ori == HORIZONTAL) {
			if (tablero[x][y+j] != 0) 
				found = true;
                        if (x>0 && tablero[x-1][y+j] != 0) 
				found = true;
                        if (x<LADOTAB-1 && tablero[x+1][y+j] != 0) 
				found = true;
		} else { 
			if (tablero[x+j][y] != 0) 
				found = true;
                        if (y>0 && tablero[x+j][y-1] != 0) 
				found = true;
                        if (y<LADOTAB-1 && tablero[x+j][y+1] != 0) 
				found = true;
		}
	}
	
	return found;
}

int main(int argc, char **argv) {
	int **tablero = 0;
	int tamanos[BARCOS] = { 5, 4, 3, 3, 2 };	
	int tableros = 0, ori = 0, x = 0, y = 0;
	char path[200]; // Pa que sooooobre
	FILE *f;
	
	srand(time(0));
	
	if (argc < 2) {
		printf("Uso: barcos <numero de tableros> [matriz]");
	} else {
		tableros = atoi(argv[1]); // Numero de tableros
		
		// Crea
		tablero = new int *[LADOTAB];
		for (int i = 0; i < LADOTAB; i++)
			tablero[i] = new int[LADOTAB];
		
		for (int tab = 0; tab < tableros; tab++) {
			// Limpia
			for (int i = 0; i < LADOTAB; i++) {
				for (int j = 0; j < LADOTAB; j++) {
					tablero[i][j] = 0;
				}
			}
	
			// Rellena
			for (int i = 0; i < BARCOS; i++) {
				ori = numero_aleatorio_entre(0,1);
				
				do {
					if (ori == HORIZONTAL)
						y = numero_aleatorio_entre(0,9-(tamanos[i]-1)-1);
					else
						y = numero_aleatorio_entre(0,9);
						
					if (ori == VERTICAL)
						x = numero_aleatorio_entre(0,9-(tamanos[i]-1)-1);
					else
						x = numero_aleatorio_entre(0,9);
					
				} while (colision(tablero, x, y, ori, tamanos[i]));
				
				for (int j = 0; j < tamanos[i]; j++) {
					if (ori == HORIZONTAL)
						tablero[x][y+j] = 1;
					else 
						tablero[x+j][y] = 1;
				}
			}
			
			// Envia al fichero
			sprintf(path,"./tablero%d.txt", 1);
			f = fopen(path,"a");
			
			if (f) {
				for (int i = 0; i < LADOTAB; i++) {
					for (int j = 0; j < LADOTAB; j++) {
						fprintf(f,"%d",tablero[i][j]);
					}
                                        if (argv[2]){
                                                fprintf(f,"\n");
                                        }
				}
				fprintf(f,"\n");
			}
			
			fclose(f); f = 0; // Voila!
		}
		
		// Recogiendo la basura
		for (int i = 0; i < LADOTAB; i++)
			delete [] tablero[i];
		delete [] tablero;
	}
	
	return 0;
}
